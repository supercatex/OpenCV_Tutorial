import cv2


def on_mouse_my_window(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        print("Mouse Move:", x, y)
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("L DOWN:", x, y, flags)
    elif event == cv2.EVENT_LBUTTONUP:
        print("L UP:", x, y, flags)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("L DB Click:", x, y, flags)
    else:
        print(event, x, y, flags, params)


window_name = "My Window"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, on_mouse_my_window)

camera = cv2.VideoCapture(0)
while camera.isOpened():
    success, frame = camera.read()
    if not success:
        continue

    cv2.imshow(window_name, frame)

    key_code = cv2.waitKey(1)
    if key_code in [27, ord('q')]:
        break
camera.release()
cv2.destroyAllWindows()
