import cv2
import os

save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera not accessible")
    exit()

print("Camera opened")
print("Press C to capture | Press Q to quit")

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera Capture", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        filename = f"{save_dir}/img_{count}.jpg"
        cv2.imwrite(filename, frame)
        print("Saved:", filename)
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
