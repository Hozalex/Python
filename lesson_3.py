# 1
def division(val1, val2):
    if val2 != 0:
        result = val1 / val2
        return result
    else:
        print("Деление на ноль")


print(division(int(input("input first number ")), int(input("input second number "))))


# 2
def user_description(name, lastname, birthday, city, email, phone):
    print(f'{name} {lastname} {birthday} {city} {email} {phone}')


user_description(name="John", lastname="Second", birthday="13.12.11", email="john@email", city="Gotham City",
                 phone="+9876554")
