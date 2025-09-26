import cv2
import os
import time

# ASCII characters from dark to bright
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_frame(image, new_width=120):
    height, width = image.shape
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)  # adjust ratio for terminal
    return cv2.resize(image, (new_width, new_height))

def frame_to_ascii(image):
    ascii_frame = ""
    for row in image:
        for pixel in row:
            ascii_frame += ASCII_CHARS[pixel // 25]
        ascii_frame += "\n"
    return ascii_frame

def play_video_in_terminal(video_path, width=120, fps=30):
    cap = cv2.VideoCapture(video_path)
    delay = 1 / fps

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = resize_frame(gray, new_width=width)
        ascii_frame = frame_to_ascii(resized)

        os.system("clear")  # clears terminal
        print(ascii_frame)
        time.sleep(delay)

    cap.release()

if __name__ == "__main__":
    video_path = "your_video.mp4" # replace with your video path
    play_video_in_terminal(video_path, width=120, fps=120 )
