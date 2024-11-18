from PIL import Image
import numpy as np
import json
import sys

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    return im

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def write(row):
    new_row = []
    for a, b, c in zip(*[iter(row)]*3):
        model = [a, b, c]
        new_pixel = [0, 0, 0]
        for i in range(3):
            if 255 in model[i][0:3]:
                new_pixel[i] = 255
        new_row.append(tuple(new_pixel))
    return new_row

argc = len(sys.argv)
argv = sys.argv
try:
    if argc <= 1:
        print("""Usage: python write.py <text>
    Text is the text you want to SubPixelWrite, also used as the file name""")
    else:
        name = argv[1]

        with open("charset.json") as file:
            charset = json.load(file)

        intext = name.upper()
        if charset.get(intext[0]):
            with Image.open(charset[intext[0]]).convert("RGB") as image:
                for i in range(1, len(intext)):
                    if charset.get(intext[i]):
                        with Image.open(charset[intext[i]]) as image2:
                            image = merge(image, image2)
                x, y = image.size
                if (mod:=x % 3):
                    image = add_margin(image, 0, 2-mod, 0, 1, (0,0,0))

                new = []
                for row in np.asarray(image):
                    new_row = write(row)
                    new.append(np.array(new_row))
                new = np.asarray(new)
                new = Image.fromarray(new.astype(np.uint8))
                new.save(f"{name}.png")

        else:
            raise ValueError("Does not fit current charset!")
except Exception as e:
    print(e)

