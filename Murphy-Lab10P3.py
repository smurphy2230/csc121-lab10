# This program stores the water usage of 4 customers in a text
# file. Data stored is account number, customer type, gallons
# used

output_file = open("water.txt", "w")

for i in range(4):
    account_number = int(input("Enter account number: "))
    account_type = input(
        "Enter R for residential, B for business account: ").upper()
    water_used = float(input("Enter gallons used: "))
    output_string = str(account_number) + " " + \
        account_type + " " + str(water_used) + "\n"
    output_file.write(output_string)

output_file.close()
