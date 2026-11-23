"""
File to detect RGB cubes, draw bounding box, and find coordinates
"""

import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    if not ret:
        break

    # Get RGB values
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]

    # Find RGB pixels
    colors = {
        "Red": (r > g * 1.5) & (r > b * 1.5),
        "Green": (g > r * 1.5) & (g > b * 1.5),
        "Blue": (b > r * 1.5) & (b > g * 1.5),
    }

    for color, mask in colors.items():
        contours, _ = cv2.findContours(
            np.uint8(mask), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )

        for contour in contours:
            # Find center of cube
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2

            # Draw bounding box and center point
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 10, (0, 0, 0), -1)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
