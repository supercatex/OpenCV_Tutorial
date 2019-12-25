import cv2


# -- 001 -- #
img = cv2.imread("./images/sample_01.jpg", cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow("My image", img)
cv2.waitKey(0)

# -- 002 -- #
cat_1 = img[105:370, 235:475, :]
cat_2 = img[195:335, 590:720, :]

cv2.imshow("Cat 1", cat_1)
cv2.imshow("Cat 2", cat_2)
cv2.waitKey(0)
