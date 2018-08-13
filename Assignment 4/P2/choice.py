#!/usr/bin/python3

import numpy
import sys
import string
import pickle

def fill_choice():
    rand_int = numpy.random.randint(1,5000,100)
    alpha = list(string.ascii_uppercase)
    int_str = dict()
    used_str = set()
    for integer in rand_int:
        #print(integer)
        uniq_str = ''
        while True:
            uniq_str = ''.join(numpy.random.choice(alpha,4))
            if uniq_str not in used_str:
                break
        int_str[integer] = uniq_str
    with open('new_int.p', 'wb') as pick_file:
        pickle.dump(int_str, pick_file)

def ask_choice(fname):
    int_str = dict()
    with open(fname, 'rb') as pick_file:
        int_str = pickle.load(pick_file)
    target = int(input('Enter number: '))
    #print(int_str)
    while target<5000 or 7000<target:
        target = int(input('Enter number: '))
    req_pairs = [(x,y) for x in int_str for y in int_str if x+y==target]
    if req_pairs == []:
        req_pairs = [(x,y) for x in int_str for y in int_str if x+y<target]
    if req_pairs == []:
        print('Not Possible')
    else:
        first_pair = req_pairs[0]
        print(int_str[first_pair[0]], first_pair[0], \
              int_str[first_pair[1]], first_pair[1])

if len(sys.argv) == 1:
    fill_choice()
else: # len(sys.argv) == 2
    filename = sys.argv[1]
    ask_choice(filename)
