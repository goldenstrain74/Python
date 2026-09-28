import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

prev_time = 0

old_x = 0
old_y = 0

direction = "BEKLIYOR"

while True:

    ret, frame = cam.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    height, width = frame.shape[:2]

    cell_width = width // 5
    cell_height = height // 5

    # FPS
    current_time = time.time()

    if prev_time != 0:
        fps = 1 / (current_time - prev_time)
    else:
        fps = 0

    prev_time = current_time

    # HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 120, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    object_found = False

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 400:

            object_found = True

            (x, y), radius = cv2.minEnclosingCircle(cnt)

            center_x = int(x)
            center_y = int(y)
            radius = int(radius)

            # Grid koordinatı
            grid_x = center_x // cell_width + 1
            grid_y = center_y // cell_height + 1

            if old_x != 0:

                diff_x = center_x - old_x
                diff_y = center_y - old_y

                threshold = 5

                if diff_x > threshold and diff_y < -threshold:
                    direction = "SAG UST"

                elif diff_x > threshold and diff_y > threshold:
                    direction = "SAG ALT"

                elif diff_x < -threshold and diff_y < -threshold:
                    direction = "SOL UST"

                elif diff_x < -threshold and diff_y > threshold:
                    direction = "SOL ALT"

                elif diff_x > threshold:
                    direction = "SAG"

                elif diff_x < -threshold:
                    direction = "SOL"

                elif diff_y > threshold:
                    direction = "ASAGI"

                elif diff_y < -threshold:
                    direction = "YUKARI"

                else:
                    direction = "BEKLIYOR"

            old_x = center_x
            old_y = center_y

            # Nesne çemberi
            cv2.circle(
                frame,
                (center_x, center_y),
                radius,
                (0, 255, 0),
                2
            )

            # Merkez noktası
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Piksel koordinatı
            cv2.putText(
                frame,
                f"X:{center_x} Y:{center_y}",
                (center_x + 10, center_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                2
            )

            # Grid koordinatı
            cv2.putText(
                frame,
                f"GRID: ({grid_x},{grid_y})",
                (center_x + 10, center_y + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )

            break

    if not object_found:

        direction = "BEKLIYOR"

        old_x = 0
        old_y = 0

    # Grid çizgileri
    for i in range(1, 5):

        cv2.line(
            frame,
            (i * cell_width, 0),
            (i * cell_width, height),
            (100, 100, 100),
            1
        )

        cv2.line(
            frame,
            (0, i * cell_height),
            (width, i * cell_height),
            (100, 100, 100),
            1
        )

    # Hücre koordinatları
    for row in range(5):

        for col in range(5):

            cv2.putText(
                frame,
                f"({col+1},{row+1})",
                (
                    col * cell_width + 5,
                    row * cell_height + 20
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35,
                (120, 120, 120),
                1
            )

    # FPS
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Hareket yönü
    cv2.putText(
        frame,
        f"Yon: {direction}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.imshow("Mavi Nesne Takibi", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

    if cv2.getWindowProperty(
        "Mavi Nesne Takibi",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

cam.release()
cv2.destroyAllWindows()