import cv2


def on_mouse_my_window(event, x, y, flags, params):
    global mode, images, btn_w

    if event == cv2.EVENT_LBUTTONDOWN:
        print("L DOWN:", x, y, flags)

        m = x // 100
        if m >= len(images):
            mode = 0
        else:
            btn_h = btn_w * images[m].shape[0] // images[m].shape[1]
            if y >= btn_h:
                mode = 0
            else:
                mode = m + 1


window_name = "My Window"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, on_mouse_my_window)

mode = 0
btn_w = 100
images = list()
images.append(cv2.imread("./images/sample_01.jpg"))
images.append(cv2.imread("./images/sample_02.jpg"))

camera = cv2.VideoCapture(0)
while camera.isOpened():
    success, frame = camera.read()
    if not success:
        continue

    if mode > 0:
        frame = images[mode - 1]

    for i, image in enumerate(images):
        w = btn_w
        h = w * image.shape[0] // image.shape[1]
        img = cv2.resize(image, (w, h))
        o = w * i
        frame[:h, o:o+w, :] = img

    cv2.imshow(window_name, frame)

    key_code = cv2.waitKey(1)
    if key_code in [27, ord('q')]:
        break
camera.release()
cv2.destroyAllWindows()
