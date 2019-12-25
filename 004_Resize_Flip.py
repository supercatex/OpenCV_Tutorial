import cv2


# -- 001 -- #
img = cv2.imread("./images/sample_01.jpg", cv2.IMREAD_COLOR)
cv2.imshow("My image", img)
cv2.waitKey(0)

# -- 002 -- #
cat_1 = img[105:370, 235:475, :]
cat_2 = img[195:335, 590:720, :]

print("Cat 1 shape:", cat_1.shape)
print("Cat 2 shape:", cat_2.shape)

cv2.imshow("Cat 1", cat_1)
cv2.imshow("Cat 2", cat_2)
cv2.waitKey(0)

# -- 004 -- #
new_cat_1 = cv2.resize(cat_1, (cat_2.shape[1], cat_2.shape[0]))
new_cat_2 = cv2.resize(cat_2, (cat_1.shape[1], cat_1.shape[0]))

new_cat_1 = cv2.flip(new_cat_1, 1)
new_cat_2 = cv2.flip(new_cat_2, 1)

img[105:370, 235:475, :] = new_cat_2
img[195:335, 590:720, :] = new_cat_1

cv2.imshow("My image", img)
cv2.waitKey(0)
