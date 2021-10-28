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
from time import time
from random import randint

parser = argparse.ArgumentParser(description='Definition of test mode')
parser.add_argument('-utm', '--use_time_mode', help='The test runs for MAX_VALUE seconds\n ', action='store_true')
parser.add_argument('-mv', '--max_value', type=int, required=True, help='The test runs for MAX_VALUE inputs\n ')
args = parser.parse_args()


def main():

    print(Fore.RED + 'PSR ' + Fore.YELLOW + ' Group 7 ' + Fore.BLUE + ' November 2021' + Style.RESET_ALL)

    if args.use_time_mode:          #if the user uses the time mode
        tstop = args.max_value      #max time set
        N = math.inf
        print('Test ends after ' + Fore.GREEN + str(tstop) + Style.RESET_ALL + ' seconds')
    else:                           #if the user uses the input mode
        tstop = math.inf
        N = args.max_value          #max inputs set
        print('Test ends after ' + Fore.GREEN + str(N) + Style.RESET_ALL + ' inputs')

    print('Pressione uma tecla para começar.')
    readchar.readchar()             #start of the test
    t1 = time()
    t2 = time()
    count = 0

    while (count < N) and (t2 - t1 < tstop):    #asks for letters until it hits number of inputs desired or time desired
        cToType = chr(randint(97, 122))                         #chooses a random lower case letter for the user to type
        print('Type the letter ' + Fore.GREEN + cToType + Style.RESET_ALL)                   #asks for the random letter
        cTyped = readchar.readchar()
        if cTyped == ' ':                                             #if the user uses the spacebar key, the test stops
            break
        elif cTyped == cToType:                             #if the user typed the correct letter, letter comes in green
            print('You typed the letter ' + Fore.BLUE + cTyped + Style.RESET_ALL)
        else:                                                  ##if the user typed the wrong letter, letter comes in red
            print('You typed the letter ' + Fore.RED + cTyped + Style.RESET_ALL)
        count = count + 1
        t2 = time()



if __name__ == '__main__':
    main()