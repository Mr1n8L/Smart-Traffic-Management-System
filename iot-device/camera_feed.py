import cv2

def capture_frame():
    cap = cv2.VideoCapture(0)  # 0 for default camera
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('captured_frame.jpg', frame)
    cap.release()

if __name__ == "__main__":
    capture_frame()
