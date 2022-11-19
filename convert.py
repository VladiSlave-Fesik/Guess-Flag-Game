from PIL import Image
from colorit import background, init_colorit

def print_flag():
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            # print(image.getpixel((x, y)))
            print(background('   ', image.getpixel((x, y))), end='')
        print()

folder = 'iso3166_resized\\'

init_colorit()
depth = 20

image = Image.open(folder+'ua.png')
image = image.resize((depth, depth))



input()
