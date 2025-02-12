import cv2

# Завантажуємо каскадні класифікатори
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Захоплення відеопотоку з камери
cap = cv2.VideoCapture(0)

# Основний цикл обробки кадрів
while True:
    # Зчитування відео з потоку
    ret, video = cap.read()
    if not ret:
        print("Помилка: Не вдалося отримати кадр з камери")
        break

    # Перетворення зображення в чорно-біле для детекції
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    # Виявлення облич у чорно-білому зображенні
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Малюємо червоний овал навколо обличчя (колір BGR: (0, 0, 255))
        center = (x + w // 2, y + h // 2)
        axes = (w // 2, h // 2)
        cv2.ellipse(video, center, axes, 0, 0, 360, (0, 0, 255), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = video[y:y + h, x:x + w]

        # Виявлення очей усередині області обличчя
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Малюємо зелений овал навколо очей (колір BGR: (0, 255, 0))
            eye_center = (ex + ew // 2, ey + eh // 2)
            eye_axes = (ew // 2, eh // 2)
            cv2.ellipse(roi_color, eye_center, eye_axes, 0, 0, 360, (0, 255, 0), 2)

    # Відображення відео на екрані
    cv2.imshow("Tracking", video)

    # Вихід із програми при натисканні клавіші Esc
    if cv2.waitKey(30) & 0xff == 27:
        break

# Вивільнення ресурсів
cap.release()
cv2.destroyAllWindows()
