import cv2
import numpy as np


canvas = None
camera = cv2.VideoCapture(0)
while camera.isOpened():
    success, frame = camera.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)

    # Detect red color.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = (0, 220, 220)
    upper = (10, 255, 255)
    mask = cv2.inRange(hsv, lower, upper)

    # Initialize canvas.
    if canvas is None:
        canvas = mask

    # Add canvas into frame.
    frame = frame.astype(np.float32)
    frame = frame / 255
    frame[:, :, 0] = frame[:, :, 0] * (1 - canvas.astype(np.float32) / 255)
    frame[:, :, 1] = frame[:, :, 1] * (1 - canvas.astype(np.float32) / 255)

    # Join canvas and frame, left for frame, right for canvas.
    image = np.zeros((frame.shape[0], frame.shape[1] * 2, frame.shape[2]))
    image[:, :frame.shape[1], :] = frame
    for i in range(3):
        image[:, frame.shape[1]:, i] = canvas

    # Show image.
    cv2.imshow("frame", image)

    # Key events.
    key_code = cv2.waitKey(1)
    if key_code == 27:          # ESC to quit the program.
        break
    elif key_code == ord('q'):  # 'q' to clear the screen.
        canvas = None
    elif key_code == 32:        # Hold space to draw.
        canvas = cv2.bitwise_or(canvas, mask)
        cv2.waitKey(1)
camera.release()
cv2.destroyAllWindows()
