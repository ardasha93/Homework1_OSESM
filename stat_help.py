# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:50:05 2020

@author: akhatova
"""
# function for reading the numbers from the file
def readNumbers():
    with open("input_stat.txt", 'r') as file:
        n = [float(line) for line in file]
    return n


# function for calculating the mean
def mean(n):
    s = 0
    for i in n:
        s += i
    return s/len(n)


# function for calculating the variance
def variance(n):
    v = 0
    m = mean(n)
    for i in n:
        v += (i-m)**2
    return v/len(n)


# function for calculating the standar variation
def stDev(n):
    var = variance(n)
    return round(var**(0.5), 2)


# printing the results
x = readNumbers()
m = mean(x)
v = variance(x)
std = stDev(x)
print(x)
print(m)
print(v)
print(std)
