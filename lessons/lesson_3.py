# 1
def division(val1, val2):
    if val2 != 0:
        result = val1 / val2
        return result
    else:
        print("Деление на ноль")


print(division(int(input("input first number ")), int(input("input second number "))))

# 2
print('_____________________________________')


def user_description(name, lastname, birthday, city, email, phone):
    print(f'{name} {lastname}, birthday {birthday}, address - {city} {email} {phone}')


user_description(name="John", lastname="Second", birthday="13.12.11", email="john@email", city="Gotham City",
                 phone="+9876554")

# 3
print('_____________________________________')


def my_func(x, y, z):
    return sum([x, y, z]) - min([x, y, z])


print(my_func(int(input("x = ")), int(input("y = ")), int(input("z = "))))

# 4
print('_____________________________________')


def exponentiation(x, y):
    if y < 0 < x:
        i = -1
        res = x
        while i > y:
            res = res * x
            y += 1
        return 1 / res
    else:
        print("input positive and negative number")
        return 0


print(exponentiation(int(input("input positive number ")), int(input("input negative number "))))

# 5
print('_____________________________________')


def number_function():
    res = 0
    print('input q for exit')
    while True:
        user_list = list(input('input you string ').split(' '))
        for i in user_list:
            if i.isdigit():
                res += int(i)
            elif i == 'q':
                print('exit program')
                return res
        print(res)


print(number_function())

# 6
print('_____________________________________')


def int_func(string):
    return str(string.lower()).title()


def big_letter(user_str):
    new_list = list()
    for i in list(user_str.split(' ')):
        new_list.append(int_func(i))

    new_string = ' '.join(new_list)
    return new_string


print(big_letter(input('input you string ')))
