import cv2


# -- 001 & 002 -- #
img = cv2.imread("./images/sample_01.jpg", cv2.IMREAD_COLOR)
cat_1 = img[105:370, 235:475, :]
cat_2 = img[195:335, 590:720, :]

cv2.imshow("My image", img)
cv2.imshow("Cat 1", cat_1)
cv2.imshow("Cat 2", cat_2)
cv2.waitKey(0)

# -- 003 -- #
cat_1[:, :, 0] = 255
cv2.imshow("Cat 1", cat_1)
cv2.waitKey(0)

cat_2[:, :, 1] = 255
cv2.imshow("Cat 2", cat_2)
cv2.waitKey(0)

img[:, :, 2] = 255
cv2.imshow("My image", img)
cv2.waitKey(0)
