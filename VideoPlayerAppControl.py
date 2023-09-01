import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.video_path = ""
        self.cap = None
        self.video_label = ttk.Label(root)
        self.playing = False

        self.create_widgets()

    def create_widgets(self):
        open_button = ttk.Button(self.root, text="Open Video", command=self.open_video)
        open_button.pack(pady=10)

        play_button = ttk.Button(self.root, text="Play/Pause", command=self.play_pause_video)
        play_button.pack()

        self.video_label.pack()

    def open_video(self):
        self.video_path = filedialog.askopenfilename(title="Select a video", filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))

        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.play_video()

    def play_video(self):
        if self.cap.isOpened() and not self.playing:
            self.playing = True
            while self.playing:
                ret, frame = self.cap.read()
                if not ret:
                    self.playing = False
                    self.cap.release()
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=image)
                self.video_label.config(image=photo)
                self.video_label.image = photo
                self.root.update_idletasks()

    def play_pause_video(self):
        if self.cap and self.cap.isOpened():
            if self.playing:
                self.playing = False
            else:
                self.playing = True
                self.play_video()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
