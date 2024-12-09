import os
import sys
import random
import math
from PIL import Image, ImageTk
import tkinter as tk

# Define image processing functions

def tile(s, m, n):
    width, height = s.size
    t = Image.new('RGB', (width * m, height * n))
    for i in range(m):
        for j in range(n):
            t.paste(s, (i * width, j * height))
    return t

def rotate(s, theta):
    return s.rotate(theta, expand=True)

def curl(s):
    width, height = s.size
    ci, cj = width // 2, height // 2
    t = Image.new('RGB', s.size)
    pixels = t.load()
    for si in range(width):
        for sj in range(height):
            theta = math.pi * math.sqrt((si - ci)**2 + (sj - cj)**2) / 256
            ti = int((si - ci) * math.cos(theta) - (sj - cj) * math.sin(theta) + ci)
            tj = int((si - ci) * math.sin(theta) + (sj - cj) * math.cos(theta) + cj)
            if 0 <= ti < width and 0 <= tj < height:
                pixels[ti, tj] = s.getpixel((si, sj))
    return t

def wave(s, n):
    width, height = s.size
    t = Image.new('RGB', s.size)
    pixels = t.load()
    for si in range(width):
        for sj in range(height):
            tj = int(sj + 20 * math.sin(2 * math.pi * si / n))
            if 0 <= tj < height:
                pixels[si, tj] = s.getpixel((si, sj))
    return t

def glass(s, n):
    width, height = s.size
    t = Image.new('RGB', s.size)
    pixels = t.load()
    for si in range(width):
        for sj in range(height):
            ti = si + random.randint(-n, n)
            tj = sj + random.randint(-n, n)
            if 0 <= ti < width and 0 <= tj < height:
                pixels[si, sj] = s.getpixel((ti, tj))
    return t

# Define fade transition function
def fade(s1, s2, n):
    res = []
    width, height = s1.size
    for k in range(n + 1):
        alpha = 1.0 * k / n
        t = Image.new('RGB', s1.size)
        pixels = t.load()
        for i in range(width):
            for j in range(height):
                c1 = s1.getpixel((i, j))
                c2 = s2.getpixel((i, j))
                r = int((1 - alpha) * c1[0] + alpha * c2[0])
                g = int((1 - alpha) * c1[1] + alpha * c2[1])
                b = int((1 - alpha) * c1[2] + alpha * c2[2])
                pixels[i, j] = (r, g, b)
        res.append(t)
    return res

# Load and process images
def load_image(directory):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    dir = os.path.join(script_directory, directory)
    return [os.path.join(dir, filename) for filename in os.listdir(dir) if filename.endswith(('.png', '.jpg'))]

def resize_image(image):
    return image.resize((800, 800), Image.LANCZOS)

def apply_filters(image):
    func = random.choice([tile, rotate, curl, wave, glass])
    if func == tile:
        return func(image, random.randint(3, 10), random.randint(3, 10))
    elif func == rotate:
        return func(image, random.uniform(0, 360))
    elif func == wave:
        return func(image, random.randint(1, 100))
    elif func == glass:
        return func(image, random.randint(1, 20))
    else:
        return func(image)

def preprocess_images(images):
    processed_images = []
    l = len(images)
    for i in range(30):
        img = images[i % l]
        image = Image.open(img)
        processed_image = resize_image(apply_filters(image))
        processed_images.append(processed_image)
    return processed_images

# Create slideshow application
def run_slideshow(processed_images):
    root = tk.Tk()
    root.title("Image Slideshow")
    root.geometry("800x800")

    label = tk.Label(root)
    label.pack(expand=True)

    def show_random_image(last_image=None):
        if not processed_images:
            return
        next_index = random.randint(0, len(processed_images) - 1)
        next_image = processed_images[next_index]

        if last_image:
            frames = fade(last_image, next_image, 5)  
            for frame in frames:
                photo = ImageTk.PhotoImage(frame)
                label.config(image=photo)
                label.image = photo
                root.update()
                root.after(50)  
        else:
            photo = ImageTk.PhotoImage(next_image)
            label.config(image=photo)
            label.image = photo

        root.after(2000, lambda: show_random_image(next_image))  

    show_random_image()
    root.mainloop()

if __name__ == '__main__':
    images = load_image('images')
    processed_images = preprocess_images(images)
    run_slideshow(processed_images)