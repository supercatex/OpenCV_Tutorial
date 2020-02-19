import cv2
import numpy as np


image_w = 640
image_h = 480


def create_ball(r, c, vx, vy, color):
    ball = {
        "r": r,
        "center": c,
        "vx": vx, "vy": vy,
        "color": color
    }
    return ball


ball_list = []
for i in range(100):
    rr = np.random.randint(10, 50 + 1)
    rx = np.random.randint(0, image_w)
    ry = np.random.randint(0, image_h)
    rvx = np.random.randint(-3, 3 + 1)
    rvy = np.random.randint(-3, 3 + 1)
    color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    b = create_ball(rr, (rx, ry), rvx, rvy, color)
    ball_list.append(b)

while True:
    image = np.zeros((image_h, image_w, 3), dtype=np.uint8)
    image[:, :] = 255

    for b in ball_list:
        cv2.circle(image, b["center"], b["r"], b["color"], 3)

    cv2.imshow("image", image)

    key_code = cv2.waitKey(1)
    if key_code == 27:
        break

    for b in ball_list:
        cx, cy = b["center"]
        new_cx = cx + b["vx"]
        new_cy = cy + b["vy"]

        if new_cy < 0:
            new_cy = 0
            b["vy"] = -b["vy"]
        if new_cy > image_h:
            new_cy = image_h
            b["vy"] = -b["vy"]
        if new_cx < 0:
            new_cx = 0
            b["vx"] = -b["vx"]
        if new_cx > image_w:
            new_cx = image_w
            b["vx"] = -b["vx"]

        b["center"] = (new_cx, new_cy)
