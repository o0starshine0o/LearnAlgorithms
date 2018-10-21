import math
import operator

from functools import reduce


def log(t):
    return math.log10(t)


def root(t):
    return t ** 0.5


def n(t):
    return t


def n_log(t):
    return t * math.log10(t)


def square(t):
    return t ** 2


def cube(t):
    return t ** 3


def exponent(t):
    # have to limit t less then 80, it's too huge
    return 2 ** min(t, 80)


def factorial(t):
    # have to limit t less then 20, it's too huge
    return reduce(operator.mul, range(1, min(t, 20) + 1))


def print_time_cost(func, *times):
    return list(map(lambda x: round(x, 10), map(func, times)))


if __name__ == '__main__':
    time = [1, 1 * 60, 1 * 60 * 60, 1 * 60 * 60 * 24, 1 * 60 * 60 * 24 * 30, 1 * 60 * 60 * 24 * 30 * 12, 1 * 60 * 60 * 24 * 30 * 12 * 100]
    for algorithm in [log, root, n, n_log, square, cube, exponent, factorial]:
        print(algorithm.__name__, ':', print_time_cost(algorithm, *time))
