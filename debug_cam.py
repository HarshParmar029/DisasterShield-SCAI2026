import cv2
cap = cv2.VideoCapture(0)
print("Opened:", cap.isOpened())
ret, frame = cap.read()
print("Read success:", ret)
if frame is not None:
    print("Frame shape:", frame.shape)
cap.release()
