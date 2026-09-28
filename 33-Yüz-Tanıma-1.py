import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        break

    # Aynalama
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Yuz Tanima", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

    if cv2.getWindowProperty(
        "Yuz Tanima",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

cam.release()
cv2.destroyAllWindows()