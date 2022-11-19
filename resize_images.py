import os
from PIL import Image

'''That code resized all images from iso3166 and save resized image to iso3166_resized'''

files = os.listdir('iso3166')
print(files)

for file in files:
    img = Image.open(f'iso3166\\{file}')
    img = img.resize((300, 200))
    img = img.convert('RGB')
    img.save(f'iso3166_resized\\{file}')

print('ok')