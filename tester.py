import png
from PIL import Image
import struct
from numpy import random
from scipy.spatial import distance
r = png.Reader(filename='pic2.png')
r2 = png.Reader(filename='pic1.png')
image = r.read()
rgbvals = [[a for a in i] for i in image[2]]


def order(vals):
    final = []
    for l in vals:
        for i in range(0, len(l), 4):
            final.append(l[i:i + 4])
    return final


ordered = order(rgbvals)
width = image[0]
height = image[1]
rgba_values = ordered
img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
pixels = img.load()

# loop through each pixel and set the rgba values
for x in range(width):
    for y in range(height):
        # get the rgba value for this pixel
        rgba = rgba_values[x % len(rgba_values)][y % len(rgba_values[x % len(rgba_values)])]

        # convert the rgba bytearray to a tuple of integers
        rgba_int = struct.unpack('BBBB', rgba)
        rgba_tuple = tuple(rgba_int)

        # set the pixel value in the image
        pixels[x, y] = rgba_tuple

# save the image to a file
img.save("output.png")
