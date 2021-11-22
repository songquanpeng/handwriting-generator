import os
import pickle

import numpy as np
from PIL import Image, ImageDraw


def paste_image(background_img, foreground_img, position, rotate=0, scale=1):
    width, height = foreground_img.size
    width = int(width * scale)
    height = int(height * scale)
    x = position[0] - width // 2
    y = position[1] - height // 2
    foreground_img = foreground_img.convert("RGBA").resize((width, height)).rotate(rotate)
    foreground_img = foreground_img.convert("RGBA")
    background_img.paste(foreground_img, (x, y), foreground_img)


def strokes2img(strokes, weight=3, output_path=None):
    x_list, y_list = [], []
    for stroke in strokes:
        for x, y in stroke:
            x_list.append(x)
            y_list.append(y)
    x_max, x_min, y_max, y_min = \
        np.array(x_list).max(), np.array(x_list).min(), np.array(y_list).max(), np.array(y_list).min()
    width, height = x_max - x_min, y_max - y_min
    width += 1
    height += 1

    # img = Image.new('RGB', (width, height), (255, 255, 255))
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    drawer = ImageDraw.Draw(img)
    for stroke in strokes:
        stroke = [(x - x_min, y - y_min) for x, y in stroke]
        drawer.line(stroke, (0, 0, 0), width=weight)
    # img = img.convert('L')
    # img.show()
    if output_path is not None:
        img.save(output_path)
    return img


def load_data(data_path):
    with open(os.path.join(data_path), 'rb') as f:
        return pickle.load(f)
