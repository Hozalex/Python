import random

# 1
in_str = None

with open("example1.txt", "a") as file1:
    while in_str != '':
        in_str = input("input string ")
        file1.writelines("%s\n" % in_str)
print("___________________ \n  #2")

# 2
count_string = 0
count_words_in_string = 0
with open("../files/example2.txt", "r", encoding="utf8") as file2:
    for string2 in file2.readlines():
        count_string += 1
        s2 = string2.split()
        print(f"quantity of words in {count_string} line is {len(s2)}")
print(f"quantity of lines in file - {count_string}")
print("___________________ \n  #3")

# 3
loser_list = []
average_salary = 0
count_lines = 0
with open("../files/example3.txt", "r", encoding="utf8") as file3:
    for string3 in file3.readlines():
        s3 = string3.split()
        if int(s3[1]) < 20:
            loser_list.append(s3[0])
        average_salary += int(s3[1])
        count_lines += 1
print(f"looser staff - {loser_list}")
print(f"average salary = {average_salary / count_lines}")
print("___________________ \n  #4")

# 4
str_count = 0
ru_set = ["Один", "Два", "Три", "Четыре"]
with open("../files/example4.txt", "r", encoding="utf8") as file4:
    for string4 in file4.readlines():
        s4 = string4.split()
        s4[0] = ru_set[str_count]
        str_count += 1
        with open("../files/new_example4.txt", "a", encoding="utf8") as n_file:
            n_file.writelines("%s\n" % ' '.join(s4))
print("___________________ \n  #5")

# 5
summary = 0
number_list = []
for i in range(10, 30):
    number_list.append(str(i))
file5 = open("../files/example5.txt", "w")
file5.write(' '.join(number_list))
file5.close()
with open("../files/example5.txt", "r") as file5:
    sum_string = file5.read().split()
    for x in sum_string:
        summary += int(x)
print(f'summ = {summary}')
print("___________________ \n  #6")

# 6
lesson_dict = {}
lesson_hour = 0
with open("../files/example6.txt", "r", encoding="utf8") as file6:
    for line in file6.readlines():
        k, *v = line.split()
        lesson_dict[k] = v
print(lesson_dict)
print("___________________ \n  #7")

# 7


