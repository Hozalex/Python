from sys import argv
from functools import reduce
from math import factorial

my_list = [2, 6, 6, 6, 8, 4, 1, 9, 1, 2, 4, 3, 2, 7, 8]
# 1
scrypt_name, work_hours, hourly_rate, bonus, = argv
print("1_________________________")
print(int(work_hours) * int(hourly_rate) + int(bonus))

# 2
print("2_________________________")
new_list = []
i = my_list[0]
for x in my_list:
    if x > i:
        new_list.append(x)
    i = x
print(list(x for x in new_list))
# неповторяющиеся значения в списке
list2 = [2, 6, 7, 4, 9, 3, 5]
print(list(x for x in list2[1:] if x > list2[list2.index(x) - 1]))

# 3
print("3_________________________")
print(list(x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0))

# 4
print("4_________________________")
print(list(x for x in my_list if my_list.count(x) == 1))

# 5
print("5_________________________")
print(reduce(lambda z, y: z + y, (x for x in range(100, 1001) if x % 2 == 0)))

# 7
print("7_________________________")


def fibo_gen():
    y = 1
    for val in range(1, 16):
        y *= val
        yield y


for el in fibo_gen():
    print(el)
