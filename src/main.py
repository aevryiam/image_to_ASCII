import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
from colorama import Style, init

init()

ASCII_CHARS = "@%#*+=-:. "

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return file_path

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def pixel_to_ascii(pixel):
    r, g, b = map(int, pixel)
    gray = int((r + g + b) / 3)
    char = ASCII_CHARS[gray * len(ASCII_CHARS) // 256]
    return char

def image_to_ascii_colored(image_path, width=100):
    try:
        image = Image.open(image_path)
    except:
        print("Failed to open image.")
        return

    image = resize_image(image, width)
    image = image.convert("RGB")
    pixels = np.array(image)

    for row in pixels:
        for pixel in row:
            r, g, b = map(int, pixel)
            ascii_char = pixel_to_ascii((r, g, b))
            print(f"\033[38;2;{r};{g};{b}m{ascii_char}", end="")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    path = select_image()
    if path:
        image_to_ascii_colored(path, width=100)
