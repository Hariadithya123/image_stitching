import cv2
import glob

paths = sorted(glob.glob("captured_images/*.jpg"))

if len(paths) < 6:
    print("Need at least 6 images for 360°")
    exit()

images = [cv2.imread(p) for p in paths]

print("Images loaded:", len(images))

stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
stitcher.setPanoConfidenceThresh(0.6)

status, pano = stitcher.stitch(images)

if status != cv2.Stitcher_OK:
    print("Stitching failed:", status)
    exit()

cv2.imwrite("stitched_360_raw.jpg", pano)
print("Raw 360 panorama saved")
