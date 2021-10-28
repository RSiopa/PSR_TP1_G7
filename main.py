#!/usr/bin/python3
# --------------------------------------------------
# A python script for complex number operations using named tuples and classes
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

import argparse
import math

import readchar
from time import time

parser = argparse.ArgumentParser(description='Definition of test mode')
parser.add_argument('-utm', '--use_time_mode', help='The test runs for MAX_VALUE seconds\n ', action='store_true')
parser.add_argument('-mv', '--max_value', type=int, required=True, help='The test runs for MAX_VALUE inputs\n ')
args = parser.parse_args()


def main():

    if args.use_time_mode:
        tstop = args.max_value      #max time set
        N = math.inf
    else:
        tstop = math.inf
        N = args.max_value      #max inputs set!

    print('Pressione uma tecla para começar.')
    readchar.readchar()
    t1 = time()
    t2 = time()
    count = 0

    while (count < N) and (t2 - t1 < tstop):
        a = t2 - t1
        print(a)
        readchar.readchar()
        count = count + 1
        t2 = time()



if __name__ == '__main__':
    main()