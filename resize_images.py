import os
from PIL import Image

files = os.listdir('iso3166')
print(files)

for file in files:
    img = Image.open(f'iso3166\\{file}')
    img = img.resize((300, 200))
    img.save(f'iso3166_resized\\{file}')

print('ok')