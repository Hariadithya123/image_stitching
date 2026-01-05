import cv2
import numpy as np

img = cv2.imread("stitched_panorama_proper.jpg")

if img is None:
    print("Stitched image not found")
    exit()

h, w = img.shape[:2]

# ---- CYLINDRICAL PROJECTION ----
f = w / 2
cyl = np.zeros_like(img)

for y in range(h):
    for x in range(w):
        theta = (x - w / 2) / f
        h_ = (y - h / 2) / f

        X = np.sin(theta)
        Y = h_
        Z = np.cos(theta)

        x_ = int(f * X / Z + w / 2)
        y_ = int(f * Y / Z + h / 2)

        if 0 <= x_ < w and 0 <= y_ < h:
            cyl[y, x] = img[y_, x_]

# ---- AUTO CROP ----
gray = cv2.cvtColor(cyl, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

coords = cv2.findNonZero(mask)
x, y, w, h = cv2.boundingRect(coords)

cropped = cyl[y:y+h, x:x+w]

# ---- FORCE 16:9 LANDSCAPE ----
target_ratio = 16 / 9
h, w = cropped.shape[:2]

if w / h > target_ratio:
    new_w = int(h * target_ratio)
    start_x = (w - new_w) // 2
    cropped = cropped[:, start_x:start_x + new_w]
else:
    new_h = int(w / target_ratio)
    start_y = (h - new_h) // 2
    cropped = cropped[start_y:start_y + new_h, :]

final = cv2.resize(cropped, (1920, 1080))

cv2.imwrite("final_panorama_clean.jpg", final)
print("Final clean landscape saved as final_panorama_clean.jpg")

