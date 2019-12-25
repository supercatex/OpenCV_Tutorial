import cv2


cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
png = cv2.imread("./images/sample_03.png", cv2.IMREAD_UNCHANGED)

camera = cv2.VideoCapture(0)

while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        w2 = w
        h2 = png.shape[0] * w2 // png.shape[1]
        mask = cv2.resize(png, (w2, h2))

        ny = y - (h2 - h) // 2
        alpha = mask[:, :, 3] / 255
        for i in range(3):
            frame[ny:ny + h2, x:x + w2, i] = frame[ny:ny + h2, x:x + w2, i] * (1 - alpha) + mask[:, :, i] * alpha

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
