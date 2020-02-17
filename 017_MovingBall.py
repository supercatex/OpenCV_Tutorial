import cv2
import numpy as np


image_w = 640
image_h = 480
ball_r = 50
ball_x = image_w // 2
ball_y = image_h // 2
ball_v = 10
ball_vy = 1
ball_vx = 1

while True:
    image = np.zeros((image_h, image_w), dtype=np.uint8)
    image[:, :] = 255

    cv2.circle(image, (ball_x, ball_y), ball_r, 0)

    cv2.imshow("image", image)

    key_code = cv2.waitKey(1)
    if key_code == 27:
        break
    elif key_code == ord('w'):
        ball_vy -= 1
    elif key_code == ord('s'):
        ball_vy += 1
    elif key_code == ord('a'):
        ball_vx -= 1
    elif key_code == ord('d'):
        ball_vx += 1
    else:
        ball_y += ball_vy
        ball_x += ball_vx

    if ball_y < 0 + ball_r:
        ball_y = 0 + ball_r
        ball_vy = -ball_vy
    if ball_y > image_h - ball_r:
        ball_y = image_h - ball_r
        ball_vy = -ball_vy
    if ball_x < 0 + ball_r:
        ball_x = 0 + ball_r
        ball_vx = -ball_vx
    if ball_x > image_w - ball_r:
        ball_x = image_w - ball_r
        ball_vx = -ball_vx
