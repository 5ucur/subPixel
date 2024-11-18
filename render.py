from PIL import Image
import numpy as np
import sys

def render(row):
    new_row = []
    for pix in row:
        #print(pix)
        new_row.append([pix[0], np.uint8(0), np.uint8(0), np.uint8(255)])
        new_row.append([np.uint8(0), pix[1], np.uint8(0), np.uint8(255)])
        new_row.append([np.uint8(0), np.uint8(0), pix[2], np.uint8(255)])
    return new_row

def subpixel(path, h=3, scale=1):
    # Open the image
    with Image.open(path) as pic:
        # Load it into an array
        image = np.asarray(pic)
        # Make a list for the new image
        new_pix_array = []
        # Go through the rows of the original image
        for row in image:
            # Render each row
            new_row = np.array(render(row))
            for n in range(h):
                new_pix_array.append(new_row)

        # Create and return the new image
        new_image = Image.fromarray(np.asarray(new_pix_array))
        x, y = new_image.size
        new_image = new_image.resize((scale*x, scale*y), resample=Image.Resampling.BOX)

        return new_image

argc = len(sys.argv)
argv = sys.argv
try:
    if argc <= 1:
        print("""Usage: python render.py <file> [height] [scale]
    File is the image you want to SubPixelRender
    Height is the multiplier of pixel height, default is 3
    Scale is the overall render size multiplier, default is 1
      Including height is needed to use scale.""")
    else:
        name, ext = argv[1].split(".")
        h = int(argv[2])
        s = int(argv[3])
        if argc == 2:
            subpixel(argv[1]).save(f"{name}_SPR.{ext}")
        elif argc == 3:
            subpixel(argv[1], h).save(f"{name}_SPR_{argv[2]}.{ext}")
        elif argc == 4:
            subpixel(argv[1], h, s).save(f"{name}_SPR_{argv[2]}_x{argv[3]}.{ext}")
except Exception as e:
    print(e)
