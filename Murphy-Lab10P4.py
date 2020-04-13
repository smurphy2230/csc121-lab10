input_file = open("water.txt", "r")

for line in input_file:
    line = line.strip("\n")
    line_items = line.split(" ")
    if line_items[1] == "R":
        if float(line_items[2]) <= 6000:
            cost_water = float(line_items[2]) * .005
        else:
            cost_water = (6000 * .005) + (float(line_items[2]) - 6000) * .007
    else:
        if float(line_items[2]) <= 8000:
            cost_water = float(line_items[2]) * .006
        else:
            cost_water = (8000 * .006) + (float(line_items[2]) - 8000) * .008
    print("Account number: " +
          line_items[0] + " " + "Water charge: " + str(cost_water))

input_file.close()
