from iso3166 import countries as cnt
from random import choice
import pyfiglet as fg
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
            print(background('    ', img.getpixel((x, y))), end='')
        print()

def main():
    hello_world = fg.Figlet(font='slant', width=300).renderText('Quess Flag')
    print(hello_world)

if __name__ == '__main__':
    main()