#!/usr/bin/python3

# Reference: https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/howto/argparse.html#id1

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--check_prime')
parser.add_argument('--range', nargs=2)
args = parser.parse_args()

def checkPrime(n):
    '''Returns True if n is Prime'''
    n=int(n)
    if (n==1):
        return False
#    print('n=',n)
    sqrt_n = math.ceil(math.sqrt(n));
    for i in range(2,sqrt_n+1):
        if n%i==0:
            return False
    return True

def nPrimesInRange(start,end):
    '''
    Return the number of primes from start to
    end (both inclusive)
    '''
    count = 0
    for i in range(start,end+1):
        if checkPrime(i):
            count += 1
    return count
            
    
arg_list = []



if args.check_prime:
    arg_list.append(int(args.check_prime))
if args.range:
    arg_list.append( int(parser.parse_args().range[0]))
    arg_list.append( int(parser.parse_args().range[1]))
if (not args.check_prime) and (not args.range):
    print('At least one of the following arguments are required: --check_prime, --range')

    exit(0)


for arg in arg_list:
    if (arg < 1 or 1000 < arg):
        print('Error : Please enter a value between 1 and 1000 only')
        exit(0)
    
if args.check_prime:
    if checkPrime(args.check_prime):
        print('Yes',end=' ')
    else:
        print('No', end=' ')
if args.range:
    ini = int(parser.parse_args().range[0])
    fin = int(parser.parse_args().range[1])
    print(nPrimesInRange(ini,fin), end=' ')
    
print()
