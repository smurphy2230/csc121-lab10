input_file = open('my_file.txt', 'r')
for line in input_file:
    print(line.strip("\n"))
