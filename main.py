from iso3166 import countries as cnt
from random import choice,shuffle
import pyfiglet as fg
import os
from PIL import Image
from colorit import background, init_colorit
from time import sleep

init_colorit()

flags_folder = 'iso3166_resized\\'
flags = os.listdir(flags_folder)

scores = 0
num_rounds = 0
lives = 3


def print_flag(img: str, folder: str = flags_folder, depth: int = 20):

    img = Image.open(folder + img)
    img = img.resize((depth, depth))

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            print(background('    ', img.getpixel((x, y))), end='')
        print()


def round():
    global lives,scores,num_rounds

    print(f'Round number {num_rounds}\nLives {lives}\nScores {scores}')

    print_flag(right_flag:= choice(flags))

    answers_list = []

    while len(answers_list) != 3:
        flag = choice(flags)
        answers_list.append(flag.replace('.png', '')) if flag not in answers_list else ...

    answers_list.append(right_flag.replace('.png', ''))

    shuffle(answers_list)

    for code in answers_list:
        country_name = cnt.get(code).name
        print(f'{country_name}|{code}')

    answer = input('\nInput a code: ')

    if answer != right_flag.replace('.png', ''):
        lives -= 1
        print(f'Wrong! Right answer - {cnt.get(right_flag.replace(".png","") ).name}|{right_flag.replace}\n')

    else:
        scores += 1
        print('Correct!\n')

    num_rounds += 1


def main():
    hello_world = fg.Figlet(font='slant', width=500).renderText('Q u e s s   F l a g')
    print(hello_world)
    print('In this game you have to guess which country is depicted on the minimalist flag')
    input('Press Enter to start game\n')

    while lives != 0:
        round()

    print(f'Your result:\n Scores - {scores} \n Number of rounds - {num_rounds}')

if __name__ == '__main__':
    main()