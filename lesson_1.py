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
l = len(a)
while l > 0:
    max = int(a[l])
    l -= 1

print(max)

# 5
profit = input("input profit ")
costs = input("input costs ")
