import cv2

# Load the cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Capture video feed from the webcam
cap = cv2.VideoCapture(0)

# Main loop for frame processing
while True:
    # Read a frame from the video feed
    ret, video = cap.read()
    if not ret:
        print("Error: Could not fetch frame from the camera")
        break

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a red ellipse around the detected face (color BGR: (0, 0, 255))
        center = (x + w // 2, y + h // 2)
        axes = (w // 2, h // 2)
        cv2.ellipse(video, center, axes, 0, 0, 360, (0, 0, 255), 2)

        roi_gray = gray[y:y + h, x:x + w]  # Region of interest in grayscale
        roi_color = video[y:y + h, x:x + w]  # Region of interest in color

        # Detect eyes within the detected face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw a green ellipse around the detected eyes (color BGR: (0, 255, 0))
            eye_center = (ex + ew // 2, ey + eh // 2)
            eye_axes = (ew // 2, eh // 2)
            cv2.ellipse(roi_color, eye_center, eye_axes, 0, 0, 360, (0, 255, 0), 2)

    # Display the video feed with detection overlays
    cv2.imshow("Tracking", video)

    # Exit the program when the Esc key is pressed
    if cv2.waitKey(30) & 0xff == 27:
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
