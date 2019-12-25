import cv2


camera = cv2.VideoCapture(0)

while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("rgb", rgb)
    cv2.imshow("gray", gray)
    cv2.imshow("binary", binary)

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
