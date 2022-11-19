from iso3166 import countries
import os

flags = os.listdir('iso3166_resized')

print(flags)


for flag in flags:
    flag = flag.replace('.png','')
    print(countries.get(flag))