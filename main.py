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
        x_delta = 0
        y_delta = 0
        if char == '\n':
            x_offset = 0
            y_offset += 4 * y_spacing
            continue
        elif char in ['，', '。']:
            x_delta = int(1.5 * x_spacing)
            y_delta = int(0.5 * y_spacing)
        try:
            strokes = strokes_dict[char]
        except KeyError:
            print(f"警告：字库中未找到「{char}」，这个字会被忽略。你可以选择用一个字库中有的相近的字代替，或者尝试更换字库。")
            continue
        char_img = strokes2img(strokes, weight)
        char_width, char_height = char_img.size
        char_width, char_height = int(char_width * scale), int(char_height * scale)

        if 2 * x_margin + x_offset + x_spacing + char_width < paper_width:
            x_offset += x_spacing + char_width
        else:
            x_offset = 0
            y_offset += char_height + y_spacing

        x = x_margin + x_offset + x_delta
        y = y_start + y_offset + y_delta

        paste_image(paper_img, char_img, (x, y), scale=scale)


def strokes_fix(strokes_dict):
    strokes_dict['，'] = strokes_dict[',']
    strokes_dict['！'] = strokes_dict['!']
    strokes_dict['？'] = strokes_dict['?']
    strokes_dict['“'] = strokes_dict['"']
    strokes_dict['“'] = strokes_dict['"']
    strokes_dict['；'] = strokes_dict[';']
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
    write_paper(paper_img, args.title, strokes_dict, x_margin=args.title_margin, y_start=args.title_start_y,
                x_spacing=args.spacing_x, y_spacing=args.spacing_y, weight=args.title_weight,
                scale=args.title_scale)
    content = '\n'.join(args.content)
    write_paper(paper_img, content, strokes_dict, x_margin=args.content_margin, y_start=args.content_start_y,
                x_spacing=args.spacing_x, y_spacing=args.spacing_y, weight=args.content_weight,
                scale=args.content_scale)

    paper_img.save(save_path)
    print(f"图片已保存至：{save_path}")
    paper_img.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--paper_width', type=int, default=1166)
    parser.add_argument('--paper_height', type=int)
    parser.add_argument('--paper_ratio', type=float, default=1.414)
    parser.add_argument('--output_path', type=str, default='results')
    parser.add_argument('--font_data', type=str, required=True)
    parser.add_argument('--spacing_x', type=int, default=10)
    parser.add_argument('--spacing_y', type=int, default=30)
    parser.add_argument('--title', type=str, required=True)
    parser.add_argument('--content', type=str, nargs='+', required=True)
    parser.add_argument('--title_weight', type=int, default=10)
    parser.add_argument('--content_weight', type=int, default=7)
    parser.add_argument('--title_scale', type=float, default=0.4)
    parser.add_argument('--content_scale', type=float, default=0.3)
    parser.add_argument('--title_margin', type=int, default=60)
    parser.add_argument('--content_margin', type=int, default=100)
    parser.add_argument('--title_start_y', type=int, default=100)
    parser.add_argument('--content_start_y', type=int, default=200)
    main(parser.parse_args())
