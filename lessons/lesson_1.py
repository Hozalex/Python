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
m = 0
i = len(a) - 1
while i >= 0:
    if int(a[i]) > m:
        m = int(a[i])
    i = i - 1
print(m)

# 5
profit = int(input("input profit "))
costs = int(input("input costs "))

if profit > costs:
    print("you have a profit")
    efficiency = ((profit - costs) / costs) * 100
    print("efficiency = %.2f%%" % efficiency)
    staff = int(input("input quantity of staff "))
    earnings = (profit - costs) / staff
    print("profit per employee %.2f" % earnings)
else:
    print("you have a damages")

# 6
a = int(input("input km per day "))
b = int(input("input required per day "))
end_day = 1
if a > b:
    print("you have reached the aim")
else:
    while a <= b:
        end_day += 1
        a += (a / 100) * 10
    print("you'll have reached the aim for %s days" % end_day)
