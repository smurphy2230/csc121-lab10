# This program asks the user to enter a string. It then converts
# all letters to uppercase and counts the frequency of each
# letter

string_input = input("Enter a string: ")
string_upper = string_input.upper()
letters = []
for i in string_upper:
    if i.isalpha():
        if i not in letters:
            num = string_upper.count(i)
            print(i, num)
            letters.append(i)
