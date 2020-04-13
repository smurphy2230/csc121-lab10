input_file = open("water.txt", "r")

for line in input_file:
    line = line.strip("\n")
    line_items = line.split(" ")
    account_number = line_items[0]
    account_type = line_items[1]
    water_used = float(line_items[2])
    if account_type == "R":
        if water_used <= 6000:
            cost_water = water_used * .005
        else:
            cost_water = (6000 * .005) + water_used - 6000 * .007
    else:
        if water_used <= 8000:
            cost_water = water_used * .006
        else:
            cost_water = (8000 * .006) + water_used - 8000 * .008
    print("Account number: " +
          account_number + " " + "Water charge: " + str(cost_water))

input_file.close()
