import os
from icecream import ic

def clear():
    os.system('clr')


def print_ar(ar):
    for i in range(ar):
        ic(i)

def plus ():
    x1 = int(input ("x1:"))
    x2 = int(input ("x2:"))
    return x1 + x2
result1 = plus()


def multiply ():
    x3 = int(input ("x3:"))
    x4 = int(input ("x4:"))
    return x3 * x4
result2 = multiply()


def division ():
    x5 = int(input ("x5:"))
    x6 = int(input ("x6:"))
    return x5 / x6
result3 = division()