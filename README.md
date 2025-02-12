# Face and Eye Tracking using OpenCV

This project demonstrates how to perform real-time face and eye detection using OpenCV's Haar cascade classifiers. The program captures video from a webcam and detects faces and eyes on each frame, drawing colored ellipses around the detected regions.

## Features

- **Face Detection**: Detects faces in a video stream using the `haarcascade_frontalface_default.xml` classifier.
- **Eye Detection**: Detects eyes within the detected face regions using the `haarcascade_eye.xml` classifier.
- **Live Video Feed**: Captures live video from your webcam and overlays the detection results in real-time.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python`)

### Installation

1. Clone this repository or download the script to your local machine.
2. Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the Haar cascade files (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) from the OpenCV GitHub repository:
   - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
   - [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

   Place these files in the same directory as the script.

## Usage

1. Run the Python script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your Python file.

2. The program will use your webcam feed to detect faces and eyes. If no webcam is found, the program will print an error.

3. Press the **ESC** key to exit the program.

## How it Works

1. The program loads pre-trained Haar cascade classifiers for face and eye detection from the XML files.
2. It captures video frames in real-time from the webcam.
3. Each frame is converted to grayscale for better performance in detection.
4. Faces and eyes are detected using the `detectMultiScale` method.
5. Detected faces are marked with a red ellipse, while detected eyes are marked with green ellipses.
6. The annotated video feed is displayed to the user.

## Example

When the program runs, the camera feed will look something like this:
![Example Output](https://via.placeholder.com/600x400.png?text=Example+Face+and+Eye+Detection)

## Dependencies

This project relies on the following dependencies:
- `opencv-python`: Main library for computer vision operations.

### Full `requirements.txt` example:
```plaintext
opencv-python
```

## License

This project is licensed under the MIT License. Free to use, modify, and distribute!

---

Happy coding! 😊
