import cv2


img = cv2.imread("./images/sample_01.jpg", cv2.IMREAD_COLOR)
cv2.imshow("My image", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("My image", gray)
cv2.waitKey(0)

cascade = cv2.CascadeClassifier(cv2.haarcascades + "haarcascade_frontalcatface.xml")

faces = cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("My image", img)
cv2.waitKey(0)

'''
For more cascade:
https://github.com/opencv/opencv/tree/master/data/haarcascades
'''
