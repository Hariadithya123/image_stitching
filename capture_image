import cv2
import os

# Create folder to save images
save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open camera")
    exit()

print("Camera opened")
print("Press 'C' to capture image")
print("Press 'Q' to quit")

img_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera - Press C to Capture | Q to Quit", frame)

    key = cv2.waitKey(1) & 0xFF  # VERY IMPORTANT LINE

    if key == ord('c'):   # press C
        img_path = os.path.join(save_dir, f"img_{img_count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Captured {img_path}")
        img_count += 1

    elif key == ord('q'): # press Q
        print("Exiting camera")
        break

cap.release()
cv2.destroyAllWindows()
