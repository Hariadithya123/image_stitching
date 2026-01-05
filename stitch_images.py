import cv2
import glob

image_paths = sorted(glob.glob("captured_images/*.jpg"))

if len(image_paths) < 2:
    print("Need at least 2 images")
    exit()

images = []
for p in image_paths:
    img = cv2.imread(p)
    if img is None:
        print("Failed to read:", p)
        exit()
    images.append(img)

print("Images loaded:", len(images))

stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)

status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite("stitched_panorama_proper.jpg", stitched)
    print("Stitching successful")
else:
    print("Stitching failed, status code:", status)
