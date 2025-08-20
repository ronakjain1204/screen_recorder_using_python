# 🎥 Screen Recorder Using Python

A lightweight, efficient screen recording tool built with Python. Designed for simplicity and performance, this application captures real-time screen activity and saves it as an MP4 video—ideal for tutorials, lectures, software demos, and troubleshooting sessions.

## 📌 Project Overview

This project addresses common limitations in existing screen recording tools such as high resource consumption, steep learning curves, and limited customization. By leveraging Python’s powerful multimedia libraries, it delivers a minimalist yet functional solution that runs smoothly even on low-end systems.

## ⚙️ Technologies Used

- **OpenCV** – For video encoding, frame display, and processing
- **Pillow (PIL)** – To capture screenshots of the screen
- **NumPy** – For efficient image array manipulation
- **screeninfo** – To dynamically detect screen dimensions across monitors

## 🚀 Features

- Real-time screen capture with live preview
- Automatic screen resolution detection
- MP4 video output using `mp4v` codec
- Adjustable frame rate (default: 5 FPS)
- Minimal CPU usage (~6% vs. 25–30% in alternatives)
- Cross-monitor compatibility

## 🧪 How It Works

1. Detects screen dimensions using `screeninfo`
2. Captures screen frames via `ImageGrab`
3. Converts frames to NumPy arrays and processes them with OpenCV
4. Displays live preview and writes frames to `recorded_video.mp4`
5. Stops recording when the `Esc` key is pressed

## 📁 File Structure

```
screen_recorder_using_python/
├── screen_capture.py                         # Main script for screen recording
├── recorded_video.mp4                        # Output video file
├── README.md                                 # Project details
├── Python Project.pdf                        # Project documentation
├── SCREEN_RECORDER_USING_PYTHON.PPT          # Project ppt
```

## 📷 Sample Output

- **Live Preview Window**: Displays the screen being recorded
- **Saved File**: `recorded_video.mp4` contains the captured session
- **Performance**: Efficient CPU usage validated via Task Manager

## 🛠 Installation

```bash
pip install opencv-python pillow numpy screeninfo
```

## ▶️ Usage

Run the script from your terminal or IDE:

```bash
python screen_capture.py
```

Press `Esc` to stop recording and save the video.

## 🌱 Future Enhancements

- 🎙️ Add audio recording support
- 🖥️ Build a GUI for easier interaction
- 🐧 Extend compatibility to macOS and Linux
- 🎞️ Improve frame rate for smoother playback
- 🔊 Synchronize audio and video streams

## 🙌 Credits

Developed by **Ronak**, Computer Science & Engineering student at Chandigarh University. Passionate about building user-centric digital products that bridge software engineering and product design.
