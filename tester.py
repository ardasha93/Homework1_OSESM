# tester.py

from linear_optimisation import readFile, solveProblem


def readFile_test():
	assert readFile() == [[9,6],[2,1,40],[1,2,50]]

def solveProblem_test():
	assert solveProblem([[9,6],[2,1,40],[1,2,50]]) == [10.0,20.0]