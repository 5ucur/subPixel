# subPixel
Write text into subpixels and render it back in upscaled previews.        
Inspired by [this awesome video](https://www.youtube.com/watch?v=SlS3FOmKUbE), "**Smaller Than Pixel Art: Sub-Pixel Art!**".

Currently only supports a small character set; see the .json file and the chars directory.

## Installation
Make sure your Python environment has [Pillow](https://python-pillow.org) and [numpy](https://numpy.org/).

## Usage

`python write.py <text>`     
- Text is the text you want to write to subpixels, also used as the output file name.
- View your text by looking at the individual subpixels, with a camera or on an older screen.         
Or, use the subPixel Renderer:

`python render.py <file> <height> <scale>`     
- File is the image you want to render the preview of.     
- Height is the multiplier of pixel height, default is 3.     
- Scale is the overall render size multiplier, default is 1.     
- Including height is needed to use scale, currently, and due to a known bug, both are currently required arguments.

## To-Do

- Fix bug with renderer requiring scale
- Negative padding (removing the 1 pixel strip if the length is 3x+1)
- Add more characters
- Display rendered image immediately?
