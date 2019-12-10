# 1
my_list = ('1', 'False', '56', True, [3, 5], {"key": 45})
for i in my_list:
    print(type(i))

# 2
my_list = input("input your list ")
for i in range(0, len(my_list)):
    print(list(my_list[i]))

# 3
month_num = int(input("input month number "))
year_time_list = ('Spring', 'Summer', 'Autumn', 'Winter')
year_time_dict = {'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11], 'Winter': [12, 1, 2]}
if 0 < month_num < 13:
    # list
    if 3 <= month_num <= 5:
        print(year_time_list[0])
    elif 6 <= month_num <= 8:
        print(year_time_list[1])
    elif 9 <= month_num <= 11:
        print(year_time_list[2])
    else:
        print(year_time_list[3])
    # dict
    for key, val in year_time_dict.items():
        if month_num in val:
            print(key)

# 4
string = input("input your string ").split(" ")
for i, val in enumerate(string, 1):
    print(i, val)

# 5
rating = [9, 5, 5, 4, 2, 1, 1]
num = int(input("input your number "))
if rating.count(num) > 1:
    rating.insert(rating.index(num) + rating.count(num), num)
else:
    rating.append(num)
    rating.sort()
    rating.reverse()
print(rating)
