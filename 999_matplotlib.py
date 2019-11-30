import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def read_frame(image_type=0):
    global camera
    success, frame = camera.read()
    if image_type == 0:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if image_type == 1:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return None


def update(i):
    global im1, im2, im4, imR, imG, imB

    rgb = read_frame(0)
    gray = read_frame(1)

    im1.set_data(rgb)
    im2.set_data(gray)

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    im4.set_ydata(hist[1:])
    ax4.set_ylim(0, max(hist[1:]))

    hist_r = cv2.calcHist([rgb], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([rgb], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([rgb], [2], None, [256], [0, 256])
    imR.set_ydata(hist_r[1:])
    imG.set_ydata(hist_g[1:])
    imB.set_ydata(hist_b[1:])
    ax3.set_ylim(0, np.max([hist_r[1:], hist_g[1:], hist_b[1:]]))


def close(event):
    if event.key in ["q", "escape"]:
        plt.close(event.canvas.figure)


camera = cv2.VideoCapture(0)

ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 2, 3)
ax4 = plt.subplot(2, 2, 4)

im1 = ax1.imshow(read_frame(0))
im2 = ax2.imshow(read_frame(1), cmap=plt.cm.gray)
im4, = ax4.plot(np.arange(1, 256, 1), np.zeros((255, 1)))
imR, = ax3.plot(np.arange(1, 256, 1), np.zeros((255, 1)), color="r")
imG, = ax3.plot(np.arange(1, 256, 1), np.zeros((255, 1)), color="g")
imB, = ax3.plot(np.arange(1, 256, 1), np.zeros((255, 1)), color="b")


ani = FuncAnimation(plt.gcf(), update, interval=50)
cid = plt.gcf().canvas.mpl_connect("key_press_event", close)
plt.show()
