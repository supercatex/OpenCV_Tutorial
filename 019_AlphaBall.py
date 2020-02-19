import cv2
import numpy as np


def create_ball(r, c, color, alpha):
    ball = {
        "r": r,
        "center": c,
        "color": color,
        "alpha": alpha
    }
    return ball


def create_ball_image(b):
    img = np.zeros((b["r"] * 2, b["r"] * 2, 3))
    cv2.circle(img, (b["r"], b["r"]), b["r"], b["color"], -1)

    alpha = np.zeros(img.shape[:2])
    cv2.circle(alpha, (b["r"], b["r"]), b["r"], b["alpha"], -1)

    return img, alpha


def join_images(img, alpha, bg, b):
    y1 = b["center"][1] - b["r"]
    y2 = b["center"][1] + b["r"]
    x1 = b["center"][0] - b["r"]
    x2 = b["center"][0] + b["r"]
    for i in range(3):
        bg[y1:y2, x1:x2, i] = bg[y1:y2, x1:x2, i] * (1 - alpha) + img[:, :, i] * alpha
    return bg


image_w, image_h = (640, 480)

image = np.zeros((image_h, image_w, 3))
image[:, :, :] = 1

ball_1 = create_ball(30, (image_w // 2, image_h // 2), (0, 0, 1), 0.5)
ball_1_img, ball_1_alpha = create_ball_image(ball_1)
image = join_images(ball_1_img, ball_1_alpha, image, ball_1)

ball_2 = create_ball(30, (image_w // 2 - 30, image_h // 2), (1, 0, 0), 0.5)
ball_2_img, ball_2_alpha = create_ball_image(ball_2)
image = join_images(ball_2_img, ball_2_alpha, image, ball_2)

ball_3 = create_ball(30, (image_w // 2 - 15, image_h // 2 - 30), (0, 1, 0), 0.5)
ball_3_img, ball_3_alpha = create_ball_image(ball_3)
image = join_images(ball_3_img, ball_3_alpha, image, ball_3)

cv2.imshow("image", image)
cv2.waitKey(0)
