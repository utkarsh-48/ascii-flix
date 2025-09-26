# ASCII Video Player

This project lets you play any video as ASCII art directly in your terminal.  
It uses Python, OpenCV, and Pillow to convert video frames into text characters.

---

## Features
- Play any video in ASCII format inside the terminal
- Adjustable width and FPS
- Simple and lightweight (just Python and a few libraries)

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ascii-video.git
cd ascii-video
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

Replace `"your_video.mp4"` in [`ascii_video.py`] with the path to your video file.

Run the script:
```bash
python ascii_video.py
```

You can adjust the width and FPS by changing the arguments in the `play_video_in_terminal` call.

---

## Requirements

See [`requirements.txt`]:

- numpy==2.2.6
- opencv-python==4.12.0.88
- pillow==11.3.0

---

## License

MIT License
