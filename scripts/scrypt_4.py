# 6
from itertools import count, cycle
from sys import argv

name, value, list_value = argv


def count_iter():
    for val in count(int(value)):
        if val == 15000:
            break
        else:
            yield val


print(list(count_iter()))


def cycle_iter():
    i = 0
    for val in cycle(list_value):
        if i == 100:
            break
        else:
            yield val
            i += 1


print(list(cycle_iter()))
