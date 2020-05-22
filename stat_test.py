# stat_test.py

from stat_help import readNumbers, mean, variance, stDev


testList = [2.0, 5.0, 7.0, 4.0, 6.0, 8.0, 9.0, 13.0, 25.0, 1.0]


def test_read_numbers():
    assert (readNumbers() == testList).all()


def test_mean():
    assert mean(testList) == 9.0


def test_variance():
    assert variance(testList) == 43.0


def test_stDev():
    assert stDev(testList) == 6.56
