from PIL import Image
from colorit import background, init_colorit

folder = 'iso3166_resized\\'

init_colorit()
depth = int(input('>>>'))

image = Image.open(folder+'xk.png')
image = image.resize((depth, depth))

for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(background('   ', image.getpixel((x, y))), end='')
    print()

input()

