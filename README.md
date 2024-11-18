# subPixel
Write text into subpixels and render it back in upscaled previews

## Installation
Make sure your Python environment has [Pillow](https://python-pillow.org) and [numpy](https://numpy.org/).

## Usage

`python write.py <text>`     
- Text is the text you want to write to subpixels, also used as the output file name.

`python render.py <file> [height] [scale]`     
- File is the image you want to render the preview of.     
- Height is the multiplier of pixel height, default is 3.     
- Scale is the overall render size multiplier, default is 1.     
- Including height is needed to use scale, currently.
