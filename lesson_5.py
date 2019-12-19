# 1
in_str = None

with open("example1.txt", "a") as file:
    while in_str != '':
        in_str = input("input string ")
        file.write(in_str + "\n")

# 2
count_string = 0
count_words_in_string = 0
with open("example2.txt", "r") as file:
    while count_string < 3:
        count_string += 1
        string = file.readline()
        s = string.split()
        print(f"quantity of words in {count_string} line is {len(s)}")
print(f"quantity of lines in file - {count_string}")
