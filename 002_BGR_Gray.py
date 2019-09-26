import cv2


camera = cv2.VideoCapture(0)

while camera.isOpened():

    success, frame = camera.read()
    if not success:
        break

    original = frame.copy()
    h, w, c = frame.shape
    cy, cx = h // 2, w // 2

    frame[:cy, :cx, 1:] = 0
    frame[:cy, cx:, :2] = 0
    frame[cy:, :cx, [0, 2]] = 0

    gray = 0
    for i in range(c):
        gray += frame[cy:, cx:, i] // c
    for i in range(c):
        frame[cy:, cx:, i] = gray

    frame[cy // 2:-cy // 2, cx // 2:-cx // 2, :] = original[cy // 2:-cy // 2, cx // 2:-cx // 2, :]

    cv2.imshow("frame", frame)
    key_code = cv2.waitKey(1)

    if key_code in [ord('q'), 27]:
        break

camera.release()
cv2.destroyAllWindows()
