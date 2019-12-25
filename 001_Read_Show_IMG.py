import cv2


# -- 001 -- #

img = cv2.imread("./images/sample_01.jpg", cv2.IMREAD_COLOR)

print(img.shape)

cv2.imshow("My image", img)

cv2.waitKey(0)
