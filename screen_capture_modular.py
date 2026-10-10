import logging
import time
from pathlib import Path

import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors


# ---------- Configuration ----------
OUTPUT_FILE = Path("recorded_video.mp4")
LOG_FILE = Path("screen_recorder.log")
FPS = 5.0
WINDOW_NAME = "Screen Recorder"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_screen_bounds():
    """Return the bounding box of the primary monitor."""
    monitors = get_monitors()

    if not monitors:
        raise RuntimeError("No monitor was detected.")

    monitor = next(
        (item for item in monitors if item.is_primary),
        monitors[0],
    )

    return (
        monitor.x,
        monitor.y,
        monitor.x + monitor.width,
        monitor.y + monitor.height,
    )


def create_video_writer(output_file, width, height, fps):
    """Create and validate the video writer."""
    codec = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        str(output_file),
        codec,
        fps,
        (width, height),
    )

    if not writer.isOpened():
        writer.release()
        raise RuntimeError(
            f"Could not open video output: {output_file}"
        )

    return writer


def record_screen():
    """Capture screen frames and save them as an MP4 video."""
    bounds = get_screen_bounds()
    left, top, right, bottom = bounds

    width = right - left
    height = bottom - top

    writer = None
    frames_recorded = 0
    start_time = time.time()

    try:
        writer = create_video_writer(
            OUTPUT_FILE, width, height, FPS
        )

        logging.info(
            "Recording started: %s, resolution=%dx%d, FPS=%.1f",
            OUTPUT_FILE, width, height, FPS,
        )

        print("Recording started. Press ESC to stop.")

        while True:
            screenshot = ImageGrab.grab(
                bbox=(left, top, right, bottom)
            )

            # Pillow returns RGB; OpenCV video frames use BGR.
            frame = cv2.cvtColor(
                np.array(screenshot),
                cv2.COLOR_RGB2BGR,
            )

            writer.write(frame)
            frames_recorded += 1

            cv2.imshow(WINDOW_NAME, frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    except KeyboardInterrupt:
        logging.info("Recording stopped by keyboard interrupt.")

    except Exception:
        logging.exception("An error occurred during recording.")
        raise

    finally:
        if writer is not None:
            writer.release()

        cv2.destroyAllWindows()

        duration = time.time() - start_time

        logging.info(
            "Recording ended. Frames=%d, duration=%.2f seconds",
            frames_recorded, duration,
        )

        print(f"Frames recorded: {frames_recorded}")
        print(f"Video saved to: {OUTPUT_FILE.resolve()}")
        print(f"Log saved to: {LOG_FILE.resolve()}")


if __name__ == "__main__":
    try:
        record_screen()
    except Exception as error:
        print(f"Recording failed: {error}")
        print(f"Check {LOG_FILE} for details.")
