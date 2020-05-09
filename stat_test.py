# stat_test.py

from stat import readFile, mean


testList = [2.0, 5.0, 7.0, 4.0, 6.0, 8.0, 9.0, 13.0, 25.0, 1.0]


def readFile_test():
    assert readFile() == testList


def mean_test():
    assert mean(testList) == 8.0
