import cv2


camera = cv2.VideoCapture(0)

prev_frame = None
while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    frame = cv2.medianBlur(frame, 5)
    if prev_frame is not None:
        mask = cv2.absdiff(frame, prev_frame)
        _, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow("mask", mask)
    else:
        prev_frame = frame

    cv2.imshow("prev", prev_frame)
    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break


camera.release()
cv2.destroyAllWindows()
