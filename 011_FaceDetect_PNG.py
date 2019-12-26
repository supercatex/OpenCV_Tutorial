import cv2


path = cv2.haarcascades + "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(path)
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

        y1 = y - (h2 - h) // 2
        y2 = y1 + h2
        if y1 < 0 or y2 >= frame.shape[0] or x + w2 >= frame.shape[1]:
            continue

        alpha = mask[:, :, 3] / 255
        for i in range(3):
            frame[y1:y2, x:x + w2, i] = frame[y1:y2, x:x + w2, i] * (1 - alpha) + mask[:, :, i] * alpha

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
