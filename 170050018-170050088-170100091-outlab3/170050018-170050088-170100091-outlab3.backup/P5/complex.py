#! /usr/bin/python3

import sys

class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def __str__(self):
        if (self.imag == int(self.imag)):
            self.imag = int(self.imag)
        if (self.real == int(self.real)):
            self.real = int(self.real)
        if (self.imag >= 0):
            return str(self.real)+"+"+str(self.imag)+"i"
        else:
            return str(self.real)+str(self.imag)+"i"
    def __add__(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result
    def __sub__(self, other):
        result = Complex()
        result.real = self.real - other.real
        result.imag = self.imag - other.imag
        return result
    def __mul__(self, other):
        result = Complex()
        result.real = self.real*other.real - self.imag*other.imag
        result.imag = self.real*other.imag + self.imag*other.real
        return result
    def __truediv__(self, other):
        abs_val = other.real**2 + other.imag**2
        result = self*Complex(other.real/abs_val, -other.imag/abs_val)
        
        return result        
        
#file_name=sys.argv[1]
a = Complex()
b = Complex()
with open('numbers.txt', 'r') as arg_file:
    nums = arg_file.read().split()
    a = Complex(float(nums[0]),float(nums[1]))
    b = Complex(float(nums[2]),float(nums[3]))

print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#print(sys.argv)
