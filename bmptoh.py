

from PIL import Image
import sys

def RGBToWord(r, g, b):
    rvalue = 0
    rvalue = rvalue + (g >> 5)
    rvalue = rvalue + ((g & 7) << 13)
    rvalue = rvalue + ((r >> 3) << 8)
    rvalue = rvalue + ((b >> 3) << 3)
    return rvalue

def main():
    args = sys.argv
    if len(args) != 2:
        print("Incorrect usage, please pass the name of the BMP file to the program.")
        return -1

    ImageFileName = args[1]
    im = Image.open(ImageFileName)

    # Convert grayscale images to RGB
    if im.mode != 'RGB':
        im = im.convert('RGB')

    print(im.format, im.size, im.mode)

    pixels = list(im.getdata())
    for px in pixels:
        if isinstance(px, int):  # If grayscale, make it an RGB tuple
            px = (px, px, px)
        print(RGBToWord(px[0], px[1], px[2]), end=',')

if __name__ == "__main__":
    main()

