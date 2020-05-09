# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:50:05 2020

@author: akhatova
"""


def readNumbers():
    with open("input_stat.txt", 'r') as file:
    t = [float(line) for line in file]
    return t


def mean(n):
    s = 0
    for i in n:
        s += i
    return s/len(n)


x = readNumbers()
print(x)
print(mean(x))
