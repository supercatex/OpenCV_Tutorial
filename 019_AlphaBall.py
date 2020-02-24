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
        left = max(0 - x1, 0)
        right = max(x2 - image_w, 0)
        top = max(0 - y1, 0)
        bottom = max(y2 - image_h, 0)

        y1 += top
        y2 -= bottom
        x1 += left
        x2 -= right

        h, w = img.shape[:2]
        img = img[top:h - bottom, left:w - right]
        alpha = alpha[top:h - bottom, left:w - right]

    for i in range(3):
        bg[y1:y2, x1:x2, i] = bg[y1:y2, x1:x2, i] * (1 - alpha) + img[:, :, i] * alpha
    return bg


image_w, image_h = (640, 480)

ball_list = []

while True:
    if np.random.randint(0, 10) == 0:
        rx = np.random.randint(0, image_w)
        ry = np.random.randint(0, image_h)
        rcr = np.random.random()
        rcg = np.random.random()
        rcb = np.random.random()
        new_ball = create_ball(1, (rx, ry), (rcb, rcg, rcr), 1)
        ball_list.append(new_ball)
    image = np.zeros((image_h, image_w, 3))
    image[:, :, :] = 1

    for b in ball_list:
        b_img, b_alpha = create_ball_image(b)
        image = join_images(b_img, b_alpha, image, b)

        if b["alpha"] > 0:
            b["alpha"] -= 0.01
            b["r"] += 1
        else:
            ball_list.remove(b)

    cv2.imshow("image", image)
    key_code = cv2.waitKey(1)
    if key_code == 27:
        break
