from iso3166 import countries as cnt
import os
from PIL import Image
from colorit import background, init_colorit

init_colorit()

flags_folder = 'iso3166_resized\\'
flags = os.listdir(flags_folder)


def print_flag(img: str, folder: str = flags_folder, depth: int = 20):

    img = Image.open(folder + img)
    img = img.resize((depth, depth))

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            print(background('   ', img.getpixel((x, y))), end='')
        print()

