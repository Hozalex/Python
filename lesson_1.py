# 1
a = 0
b = 10
print(a, b)

# 2
a = int(input("input number "))
b = input("input string ")
print(a, b)

# 3
n = input("input number - ")
print(f'{int(n) + int(n + n) + int(n + n + n)}')

# 4
a = input("input number ")
max = 0
i = len(a)-1
while i >= 0:
    if int(a[i]) > max:
        max = int(a[i])
    i = i-1
print(max)

# 5
profit = input("input profit ")
costs = input("input costs ")
