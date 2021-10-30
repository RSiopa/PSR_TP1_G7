#!/usr/bin/python3

import argparse
import math
from colorama import Fore, Back, Style
import readchar
from time import time, ctime
import random
import string
from collections import namedtuple

Input = namedtuple('Input', ['requested', 'received', 'duration'])

parser = argparse.ArgumentParser(description='Definition of test mode')
parser.add_argument('-mv', '--max_value', type=int, required=True, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.\n ')
parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.\n ')
args = vars(parser.parse_args())
print(args)

def main():
    seconds = time()
    print(Fore.RED + 'PARI' + Style.RESET_ALL + ' Typing Test, P2, Grupo 7, ' + ctime(seconds))
    print('Test running up to ' + str(args['max_value']) + ' seconds.')

    if args['use_time_mode']:
        tstop = args['max_value']      #max time set
        N = math.inf
    else:
        tstop = math.inf
        N = args['max_value']     #max inputs set!

    print('Press any key to start the test')
    readchar.readchar()
    count = 0
    t1 = time()
    t2 = time()
    save = []

    while (count < N) and (t2 - t1 < tstop):
        to_type = random.choice(string.ascii_lowercase)
        print('Type letter ' + to_type)
        t3 = time()
        typed = readchar.readchar()
        t4 = time()
        if typed == ' ':
            exit()
        if typed == to_type:
            print('You typed letter ' + Fore.GREEN + typed + Style.RESET_ALL)
        else:
            print('You typed letter ' + Fore.RED + typed + Style.RESET_ALL)

        save.append(Input(requested = to_type, received = typed, duration = (t4 - t3)))
        count = count + 1
        t2 = time()

    print('Current test duration (' + str(t2-t1) + ') exceeds maximum of ' + str(args['max_value']))
    print(Fore.BLUE + 'Test Finished!' + Style.RESET_ALL)
    # Calcular estatísticas
    print(save)
    test_duration = t2-t1
    test_start = ctime(t1)
    test_end = ctime(t2)
    number_of_types = len(save)
    number_of_hits = 0
    type_average_duration = 0
    type_hit_average_duration = 0
    for i in range len(save):
        if save[i].requested == save[i].received:
            number_of_hits += 1
        type_average_duration = save[i].duration + type_average_duration

    type_average_duration = type_average_duration/number_of_types
    accuracy = number_of_hits/number_of_types


if __name__ == '__main__':
    main()