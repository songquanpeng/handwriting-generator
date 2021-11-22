import argparse
import os

from PIL import Image

from utils import paste_image, load_data, strokes2img


def write_paper(paper_img, chars, strokes_dict, x_margin, y_start, x_spacing, y_spacing, weight=5, scale=1):
    x_offset = 0
    y_offset = 0
    paper_width, paper_height = paper_img.size
    for i in range(len(chars)):
        char = chars[i]
        if char == '\n':
            x_offset = 0
            y_offset += 4 * y_spacing
            continue
        strokes = strokes_dict[char]
        char_img = strokes2img(strokes, weight)
        char_width, char_height = char_img.size
        char_width, char_height = int(char_width * scale), int(char_height * scale)

        if 2 * x_margin + x_offset + x_spacing + char_width < paper_width:
            x_offset += x_spacing + char_width
        else:
            x_offset = 0
            y_offset += char_height + y_spacing

        x = x_margin + x_offset
        y = y_start + y_offset

        paste_image(paper_img, char_img, (x, y), scale=scale)


def strokes_fix(strokes_dict):
    strokes_dict['，'] = strokes_dict[',']
    strokes_dict['！'] = strokes_dict['!']
    strokes_dict['？'] = strokes_dict['?']
    strokes_dict['“'] = strokes_dict['"']
    strokes_dict['“'] = strokes_dict['"']
    # strokes_dict['‘'] = strokes_dict["'"]
    # strokes_dict['’'] = strokes_dict["'"]
    return strokes_dict


def main(args):
    strokes_dict = load_data(args.font_data)
    strokes_dict = strokes_fix(strokes_dict)

    os.makedirs(args.output_path, exist_ok=True)
    save_path = os.path.join(args.output_path, f"{args.title}.png")
    if args.paper_height is None:
        args.paper_height = int(args.paper_width * args.paper_ratio)
    width, height = args.paper_width, args.paper_height
    paper_img = Image.new('RGB', (width, height), (255, 255, 255))
    write_paper(paper_img, args.title, strokes_dict, x_margin=60, y_start=100, x_spacing=20, y_spacing=2, weight=10,
                scale=0.4)
    content = '\n'.join(args.content)
    write_paper(paper_img, content, strokes_dict, x_margin=100, y_start=200, x_spacing=20, y_spacing=25, weight=7,
                scale=0.3)

    paper_img.save(save_path)
    paper_img.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--paper_width', type=int, default=1166)
    parser.add_argument('--paper_height', type=int)
    parser.add_argument('--paper_ratio', type=float, default=1.414)
    parser.add_argument('--output_path', type=str, default='results')
    parser.add_argument('--font_data', type=str, required=True)
    parser.add_argument('--spacing_x', type=int, default=10)
    parser.add_argument('--spacing_y', type=int, default=20)
    parser.add_argument('--title', type=str, required=True)
    parser.add_argument('--content', type=str, nargs='+', required=True)
    main(parser.parse_args())
