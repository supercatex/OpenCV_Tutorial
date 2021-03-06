import cv2


camera = cv2.VideoCapture(0)

prev_frame = None
while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    if prev_frame is not None:
        mask = cv2.absdiff(frame, prev_frame)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow("mask", mask)

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

    prev_frame = frame

camera.release()
cv2.destroyAllWindows()
