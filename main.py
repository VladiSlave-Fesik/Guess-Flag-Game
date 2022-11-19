from iso3166 import countries
import os

print(files:=os.listdir('iso3166_resized'))

for file in files:
    file = file.replace('.png','')
    print(countries.get(file))