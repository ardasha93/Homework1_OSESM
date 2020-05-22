# stat_test.py

from stat_help import readNumbers, mean, variance, stDev


testList = [2.0, 5.0, 7.0, 4.0, 6.0, 8.0, 9.0, 13.0, 25.0, 1.0]


def readNumbers_test():
    assert readNumbers() == testList


def mean_test():
    assert mean(testList) == 9.0


def variance_test():
    assert variance(testList) == 43.0


def stDev_test():
    assert stDev(testList) == 6.56
