#!/usr/bin/python3
# --------------------------------------------------
# A python script used for a typing test
# Rafael Inacio Siopa Nª84905
# Pedro Miguel Durães de Carvalho Nº84670
# João Pedro Tira Picos Costa Nunes Nº89201
# Frederico Ribeiro e Martins Nº92760
# Grupo 7, PSR, November 2021.
# --------------------------------------------------

import argparse
import math
from colorama import Fore, Back, Style
import readchar
from time import time, ctime
import random
import string
from collections import namedtuple
import json

Input = namedtuple('Input', ['requested', 'received', 'duration'])      # initiation of namedtuple Input

parser = argparse.ArgumentParser(description='Definition of test mode')     # arguments
parser.add_argument('-mv', '--max_value', type=int, required=True, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.\n ')
parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.\n ')
args = vars(parser.parse_args())
print(args)

def main():
    seconds = time()
    print(Fore.RED + 'PSR TP1' + Style.RESET_ALL + ' Typing Test, P2, Grupo 7, ' + ctime(seconds))

    if args['use_time_mode']:       # if the user uses the time mode
        tstop = args['max_value']      # max time set
        N = math.inf                    # max indexes will never be hit
        print('Test ends after ' + Fore.GREEN + str(tstop) + Style.RESET_ALL + ' seconds')
    else:                           # if the user uses the input mode
        tstop = math.inf            # max time will never be hit
        N = args['max_value']     # max inputs set
        print('Test ends after ' + Fore.GREEN + str(N) + Style.RESET_ALL + ' inputs')

    print('Press any key to start the test')
    readchar.readchar()         # start of the test
    count = 0
    t1 = time()
    t2 = time()
    save = []

    while (count < N) and (t2 - t1 < tstop):   # asks for letters until it hits number of inputs desired or time desired
        to_type = random.choice(string.ascii_lowercase)     # chooses a random lower case letter for the user to type
        print('Type letter ' + Fore.BLUE + to_type + Style.RESET_ALL)   # asks for the random letter
        t3 = time()
        typed = readchar.readchar()     # stores typed key and time of reaction
        t4 = time()
        if typed == ' ':        # if the user uses the spacebar key, the test stops
            break
        if typed == to_type:    # if the user typed the correct letter, letter comes in green
            print('You typed letter ' + Fore.GREEN + typed + Style.RESET_ALL)
        else:                   # if the user typed the wrong letter, letter comes in red
            print('You typed letter ' + Fore.RED + typed + Style.RESET_ALL)

        save.append(Input(requested = to_type, received = typed, duration = (t4 - t3))) # adds values to Input
        count = count + 1
        t2 = time()

    print('Current test duration (' + str(t2-t1) + ') exceeds maximum of ' + str(args['max_value']))
    print(Fore.BLUE + 'Test Finished!' + Style.RESET_ALL)

    # Statistics' calculations
    test_duration = t2-t1
    test_start = ctime(t1)
    test_end = ctime(t2)
    number_of_types = len(save)
    number_of_hits = 0
    type_average_duration = 0
    type_hit_average_duration = 0
    type_miss_average_duration = 0

    for i in range(len(save)):
        if save[i].requested == save[i].received:
            number_of_hits += 1
            type_hit_average_duration = save[i].duration + type_hit_average_duration
        else:
            type_miss_average_duration = save[i].duration + type_miss_average_duration
        type_average_duration = save[i].duration + type_average_duration

    type_average_duration = type_average_duration/number_of_types
    accuracy = number_of_hits/number_of_types
    if number_of_hits == number_of_types:       # if user hits every key correctly
        type_miss_average_duration = 0
    else:
        type_miss_average_duration = type_miss_average_duration / (number_of_types - number_of_hits)
    if number_of_hits == 0:                     # if user misses every key correctly
        type_hit_average_duration = 0
    else:
        type_hit_average_duration = type_hit_average_duration/number_of_hits

    dic = {'accuracy': accuracy, 'inputs': save, 'number_of_hits': number_of_hits,          # dictionary
           'number_of_types': number_of_types, 'test_duration': test_duration,
           'test_end':test_end, 'test_start':test_start, 'type_average_duration':type_average_duration,
           'type_hit_average_duration' :type_hit_average_duration, 'type_miss_average_duration:':type_miss_average_duration}

    print(json.dumps(dic, sort_keys=False, indent=4))   # dictionary print

if __name__ == '__main__':
    main()