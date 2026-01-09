import cv2
import numpy as np

img = cv2.imread("stitched_360_raw.jpg")

if img is None:
    print("Image not found")
    exit()

# Remove curved black borders only
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

coords = cv2.findNonZero(mask)
x, y, w, h = cv2.boundingRect(coords)

clean = img[y:y+h, x:x+w]

cv2.imwrite("final_360_equirectangular.jpg", clean)
print("Saved final_360_equirectangular.jpg")
