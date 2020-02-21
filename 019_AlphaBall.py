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

    if y1 < 0 or x1 < 0 or y2 >= image_h or x2 >= image_w:
        cv2.waitKey(0)

    # right = max(x2 - image_w, 0)
    # left = max(0 - x1, 0)
    # top = max(0 - y1, 0)
    # bottom = max(y2 - image_h, 0)
    # y1 += top
    # y2 -= bottom
    # x1 += left
    # x2 -= right
    #
    # print(y1, y2, x1, x2)
    # print(top, bottom, left, right)
    # print(bg[y1:y2, x1:x2, :].shape, img[top:img.shape[0]-bottom, left:img.shape[1]-right, :].shape)

    for i in range(3):
        bg[y1:y2, x1:x2, i] = bg[y1:y2, x1:x2, i] * (1 - alpha) + img[:, :, i] * alpha
    return bg


image_w, image_h = (640, 480)

ball_1 = create_ball(1, (image_w // 2, image_h // 2), (0, 0, 1), 1)

while True:
    image = np.zeros((image_h, image_w, 3))
    image[:, :, :] = 1

    ball_1_img, ball_1_alpha = create_ball_image(ball_1)
    image = join_images(ball_1_img, ball_1_alpha, image, ball_1)

    if ball_1["alpha"] > 0:
        ball_1["alpha"] -= 0.01
        ball_1["r"] += 0
    else:
        rx = np.random.randint(30, image_w - 30)
        ry = np.random.randint(30, image_h - 30)
        rcr = np.random.random()
        rcg = np.random.random()
        rcb = np.random.random()
        ball_1 = create_ball(30, (rx, ry), (rcb, rcg, rcr), 1)

    cv2.imshow("image", image)
    key_code = cv2.waitKey(1)
    if key_code == 27:
        break
