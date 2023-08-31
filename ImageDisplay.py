import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Display")

        self.image_path = ""
        self.image_label = ttk.Label(root)

        self.create_widgets()

    def create_widgets(self):
        open_button = ttk.Button(self.root, text="Open Image", command=self.open_image)
        open_button.pack(pady=10)

        self.image_label.pack()

    def open_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an image", filetypes=(("Image files", "*.jpg *.png"), ("All files", "*.*")))

        if self.image_path:
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(image=image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

root = tk.Tk()
app = ImageDisplayApp(root)
root.mainloop()
