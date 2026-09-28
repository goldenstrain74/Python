import cv2

kamera= cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    cv2.imshow("Kamera", frame)

    key = cv2.waitKey(1)

    if key == 27 or cv2.getWindowProperty("Kamera", cv2.WND_PROP_VISIBLE) < 1:
        break
    
kamera.release()
cv2.destroyAllWindows()