try:
    from iso3166 import countries as cnt
    from random import choice, shuffle
    import pyfiglet as fg
    import os
    from PIL import Image
    from colorit import background, init_colorit
    from time import sleep, time

except ImportError as error:
    print(error)
    input('Press Enter to close game\n')

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


def open_flag(img_name: str, folder:str='iso3166\\'):
    img = Image.open(folder + img_name)

    img.save('a.png')

    img2 = Image.open('a.png')
    img2 = img2.convert('RGB')
    img2.show()


def del_a():
    os.remove('a.png')


def inf_lives():
    global lives
    lives = 2 ** 20


def help_():
    print('''
    List of all commands:
    help - to see all commands
    inf_lives - you will never lose
    open - open a original photo of flag
    ''')


def round_():
    global lives, scores, num_rounds

    print(f'Round number {num_rounds}\nLives {lives}\nScores {scores}\n')

    print_flag(right_flag := choice(flags))

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

    while answer not in answers_list and answer not in commands:
        answer = input('You type incorrect code.\nInput a code: ')

    if answer in commands:
        if answer == 'open':
            open_flag(right_flag)
            del_a()
            answer = input('\nInput a code: ')
            while answer not in answers_list:
                answer = input('You type incorrect code.\nInput a code: ')

        else:
            commands[answer]()

            answer = input('\nInput a code: ')
            while answer not in answers_list:
                answer = input('You type incorrect code.\nInput a code: ')

    if answer != right_flag.replace('.png', ''):
        lives -= 1
        print(
            f'Wrong! Right answer - {cnt.get(right_flag.replace(".png", "")).name}|{right_flag.replace(".png", "")}\n')


    else:
        scores += 1
        print('Correct!\n')


    flags.remove(right_flag)

    sleep(1.25)
    num_rounds += 1


def main():
    hello_world = fg.Figlet(font='slant', width=500).renderText('Q u e s s   F l a g')
    print(hello_world)
    print('In this game you have to guess which country is depicted on the minimalist flag. If you want to know all '
          'commands type help')
    ans = input('Press Enter to start game\n')

    if ans == 'help':
        help_()

    while lives != 0 and scores != 250 and len(flags) != 0:
        round_()

    if scores == 250:
        win = fg.Figlet(font='slant', width=500).renderText('You MEGA Win!')
        print(win)

    if len(flags) == 0:
        win = fg.Figlet(font='slant', width=500).renderText('You Win!')
        print(win)

    print(f'Your result:\n Scores - {scores} \n Number of rounds - {num_rounds}')


commands = {'help': help_, 'inf_lives': inf_lives, 'open': open_flag}

if __name__ == '__main__':
    main()
    input('Press Enter to close game\n')
