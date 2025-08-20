import cv2  # OpenCV library for handling video capture, processing, and display
from PIL import ImageGrab  # To capture screenshots (grab the screen) as an image
import numpy as np  # NumPy is used to handle arrays and convert images into arrays for OpenCV
from screeninfo import get_monitors  # To retrieve information about connected monitors (screen dimensions)


# Loop through all connected monitors and get the screen dimensions (x, y, width, height)
for m in get_monitors():
    x: int = m.x       # Top-left x-coordinate of the monitor
    y: int = m.y       # Top-left y-coordinate of the monitor
    width: int = m.width   # Width of the monitor in pixels
    height: int = m.height # Height of the monitor in pixels

# Video encoding setup
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")  # Specify the video codec (MP4 format)
captured_video = cv2.VideoWriter("recorded_video.mp4", fourcc, 5.0, (width, height))  # Initialize the video writer

# Main loop to capture the screen continuously
while True:
    # Capture the screen within the specified bounding box (monitor dimensions)
    img = ImageGrab.grab(bbox=(x, y, width, height))

    # Convert the captured image to a NumPy array (required for OpenCV operations)
    np_img = np.array(img)

    # Convert the color from BGR (used by OpenCV) to RGB (used by PIL)
    cvt_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)

    # Display the captured frame in a window called "Video capture"
    cv2.imshow("Video capture", cvt_img)

    # Write the current frame to the video file
    captured_video.write(cvt_img)

    # Wait for 20 milliseconds between frames and check for the 'Esc' key (ASCII 27)
    key = cv2.waitKey(20)
    if key == 27:  # If 'Esc' key is pressed, break the loop
        break

# Release resources and close all OpenCV windows
captured_video.release()  # Release the video writer
cv2.destroyAllWindows()