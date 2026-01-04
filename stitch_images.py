import cv2
import glob

# Load all captured images
image_paths = sorted(glob.glob("captured_images/*.jpg"))

if len(image_paths) < 2:
    print("Need at least 2 images to stitch")
    exit()

images = []
for path in image_paths:
    img = cv2.imread(path)
    images.append(img)

print(f"Loaded {len(images)} images")

# Create stitcher
stitcher = cv2.Stitcher_create()

status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite("stitched_panorama.jpg", stitched)
    print("Stitching successful")
    print("Saved as stitched_panorama.jpg")
else:
    print("Stitching failed. Status code:", status)
