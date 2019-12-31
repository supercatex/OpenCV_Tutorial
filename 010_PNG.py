import cv2


img1 = cv2.imread("./images/sample_02.jpg", cv2.IMREAD_COLOR)
print("IMG 1:", img1.shape)
cv2.imshow("img1", img1)
cv2.waitKey(0)

img2 = cv2.imread("./images/sample_03.png", cv2.IMREAD_UNCHANGED)
print("IMG 2:", img2.shape)
cv2.imshow("img2", img2)
cv2.waitKey(0)

cascade = cv2.CascadeClassifier(cv2.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    w2 = w
    h2 = img2.shape[0] * w2 // img2.shape[1]
    mask = cv2.resize(img2, (w2, h2))

    ny = y - (h2 - h) // 2
    alpha = mask[:, :, 3] / 255
    for i in range(3):
        img1[ny:ny+h2, x:x+w2, i] = img1[ny:ny+h2, x:x+w2, i] * (1 - alpha) + mask[:, :, i] * alpha

cv2.imshow("img1", img1)
cv2.waitKey(0)
