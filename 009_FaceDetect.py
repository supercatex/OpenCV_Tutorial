import cv2


cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
