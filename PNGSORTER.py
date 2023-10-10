import png
from PIL import Image
import Loader
from threading import Thread
import math
from time import sleep
import random
from scipy.spatial import distance
import itertools
r = png.Reader(filename = 'mona.png')
r2 = png.Reader(filename = 'point.png')
colors = []
colors2 = []
ordered = []
ordered2 = []
def order(vals):
    final = []
    for l in vals:
        Loader.iterator += 1
        for i in range(0, len(l), 4):
            final.append(l[i:i+4])
    return final
def write(o):
    f = open("test.txt", "w")
    for r in o:
        f.write(str(r) + "\n")
    f.close()
def findColors(o):
    new_o = []
    for elem in o:
        if elem not in new_o:
            new_o.append(elem)
        Loader.iterator += 1
    return new_o
def Print(imge, clrs):
    image = imge
    width = image[0]
    height = image[1]
    rgba_values = clrs
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            rgba = rgba_values[(y * width) + x]
            pixels[x, y] = tuple(rgba)
    img.save(str(random.random())+".png")
def sort(clrs, cc):
    closest_index = distance.cdist([cc], clrs).argmin()
    Loader.iterator +=1
    return closest_index
def Main():
    global colors
    global colors2
    global ordered
    global ordered2
    image = r.read()
    image2 = r2.read()
    rgbvals = [[a for a in i ]for i in image[2]]
    rgbvals2 = [[a for a in i ]for i in image2[2]]
    Loader.setLoader(len(rgbvals), "ordering 1st image")
    ordered = order(rgbvals)
    Loader.setLoader(len(rgbvals2), "ordering 2nd image")
    ordered2 = order(rgbvals2)
    Loader.setLoader(len(ordered), "finding equivalent colors for image 1")
    currentSet = [o for o in ordered]
    replacers2 = [None for i in range(len(ordered2))]
    dist = random.randrange(2,9)
    for i in range(0,dist):
        try:
            for c in range(len(ordered2)):
                c = i + (dist*c)
                x = sort(currentSet, ordered2[c])
                replacers2[c] = currentSet[x]
                currentSet.pop(x)
                Loader.iterator +=1
        except:
            continue
    print(len(replacers2))
    Loader.setLoader(len(ordered), "writing image 1")
    final = []
    for c in ordered:
        final.append(replacers2[ordered.index(c)])
        Loader.iterator +=1
    Print(image, final)
    Loader.setLoader(len(ordered2), "finding equivalent colors for image 2")
    currentSet = [o for o in ordered2]
    replacers = [None for i in range(len(ordered))]
    dist = random.randrange(2,9)
    for i in range(0,dist):
        try:
            for c in range(len(ordered)):
                c = i + (dist * c)
                x = sort(currentSet, ordered[c])
                replacers[c] = currentSet[x]
                currentSet.pop(x)
                Loader.iterator +=1
        except:
            continue
    Loader.setLoader(len(ordered2), "writing image 2")
    final = []
    for c in ordered2:
        final.append(replacers[ordered2.index(c)])
        Loader.iterator +=1
    Print(image2, final)
    Loader.stop = True
Loader.startLoader()
Main()
print("DONE!!!!")
