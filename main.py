try:
    from random import choice, shuffle
    import os
    import sys
    from PIL import Image
    from time import sleep, time

except ImportError as error:
    print(error)
    input('Press Enter to close game\n')

with open('iso3166_names.txt', 'r') as f:
    lines = f.readlines()

countries = {}

for line in lines:
    code, name = line.strip().split('|')
    countries[code] = name

flags_folder = 'iso3166_resized\\'
flags = os.listdir(flags_folder)
len_flags = len(flags)

hello_world = '''
   ____                                           ______   __                 
  / __ \    __  __   ___     _____   _____       / ____/  / /  ____ _   ____ _
 / / / /   / / / /  / _ \   / ___/  / ___/      / /_     / /  / __ `/  / __ `/
/ /_/ /   / /_/ /  /  __/  (__  )  (__  )      / __/    / /  / /_/ /  / /_/ / 
\___\_\   \__,_/   \___/  /____/  /____/      /_/      /_/   \__,_/   \__, /  
                                                                     /____/   
'''

mega_win = '''
__  __               __  __________________       _       ___       __
\ \/ /___  __  __   /  |/  / ____/ ____/   |     | |     / (_)___  / /
 \  / __ \/ / / /  / /|_/ / __/ / / __/ /| |     | | /| / / / __ \/ / 
 / / /_/ / /_/ /  / /  / / /___/ /_/ / ___ |     | |/ |/ / / / / /_/  
/_/\____/\__,_/  /_/  /_/_____/\____/_/  |_|     |__/|__/_/_/ /_(_)   
'''

win = '''
__  __               _       ___       __
\ \/ /___  __  __   | |     / (_)___  / /
 \  / __ \/ / / /   | | /| / / / __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / / / / /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_(_)  
'''

lose = '''
    __                            __
   / /   ____  ________       _ _/_/
  / /   / __ \/ ___/ _ \     (_) /  
 / /___/ /_/ (__  )  __/    _ / /   
/_____/\____/____/\___/    (_) /    
                             |_|  
'''

scores = 0
num_rounds = 0
lives = 3


def init_colorit():
    if sys.platform.startswith("win32"):
        os.system("cls")
    elif sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
        os.system("clear")


def color(text, rgb):
    return "\033[38;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )


def color_ansi(text, color):
    return "{}{}\033[0m".format(color, text)


def background(text, rgb):
    return "\033[48;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )


def print_flag(img: str, folder: str = flags_folder, depth: int = 20):
    global output

    img = Image.open(folder + img)
    img = img.resize((depth, depth))
    o = ''
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            o += background('    ', img.getpixel((x, y)))
        o += '\n'
    print(o)
    output += o


def open_flag(folder: str = 'iso3166\\'):
    global right_flag

    try:
        img = Image.open(folder + right_flag)
    except:
        img = Image.open('iso3166_resized\\' + right_flag)

    img.save('a.png')

    img2 = Image.open('a.png')
    img2 = img2.convert('RGBA')
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
    reset - overwrites the output in the console, needed when switching the console full screen mode
    exit - exit 
    ''')


def exit_():
    del_a()
    exit()


def reset():
    os.system('cls')
    print(output)


def round_():
    global lives, scores, num_rounds, right_flag, output
    output = ''

    o = f'Round number {num_rounds}\nLives {lives}\nScores {scores}\n'
    print(o)
    output += o

    print_flag(right_flag := choice(flags))
    answers_list = []

    while len(answers_list) != 3:
        flag = choice(flags)
        answers_list.append(flag.replace('.png', '')) if flag not in answers_list else ...

    answers_list.append(right_flag.replace('.png', ''))

    shuffle(answers_list)

    o = ''
    for code in answers_list:
        country_name = countries.get(code)
        o += f'{country_name}|{code}\n'
    print(o)
    output += o

    answer = input('\nInput a code: ').lower()

    while answer not in answers_list:
        if answer in commands:
            commands[answer.lower()]()
            answer = input('Input a code: ').lower()
        else:
            answer = input('You type incorrect code.\nInput a code: ').lower()

    if answer != right_flag.replace('.png', ''):
        lives -= 1
        print(
            f'Wrong! Right answer - {countries.get(right_flag.replace(".png", ""))}|{right_flag.replace(".png", "")}\n')

    else:
        scores += 1
        print('Correct!\n')

    flags.remove(right_flag)

    sleep(1.25)
    num_rounds += 1


def main():
    init_colorit()

    print(hello_world)
    print('In this game you have to guess which country is depicted on the minimalist flag. If you want to know all '
          'commands type help')
    ans = input('Press Enter to start game\n')

    if ans == 'help':
        help_()

    while True:
        round_()
        if scores == len_flags:
            res = mega_win
            break
        elif len(flags) == 0:
            res = win
            break
        elif lives == 0:
            res = lose
            break
    print(res)
    print(f'Your result:\n Scores - {scores} \n Number of rounds - {num_rounds}')


commands = {'help': help_, 'inf_lives': inf_lives, 'open': open_flag, 'exit': exit_, 'reset': reset}

if __name__ == '__main__':
    main()
    input('Press Enter to close game\n')
