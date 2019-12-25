import cv2


camera = cv2.VideoCapture(0)

while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
