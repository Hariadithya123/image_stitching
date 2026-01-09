import cv2
import os

save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera error")
    exit()

print("360 CAPTURE MODE")
print("Rotate slowly in a circle")
print("Capture 8–12 images")A
print("Make sure LAST image overlaps FIRST")
print("Press C to capture | Q to quit")

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, f"Frames captured: {count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("360 Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        cv2.imwrite(f"{save_dir}/img_{count}.jpg", frame)
        print(f"Captured img_{count}.jpg")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
