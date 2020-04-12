# This program asks user to input the time in a particular format. It then
# verifies the format is several ways. Correct input results in output of time
# entered without colons

time_input = input("Enter the time in the format of hh:mm:ss: ")

colon_count = time_input.count(":")
time_list = time_input.split(":")

if colon_count != 2:
    print("Must separete hour, minute and second with colons.")
elif not time_list[0].isdigit() or len(time_list[0]) != 2:
    print("Hour must be a 2 digit number.")
elif not time_list[1].isdigit() or len(time_list[1]) != 2:
    print("Minute must be a 2 digit number.")
elif not time_list[2].isdigit() or len(time_list[2]) != 2:
    print("Seonds must be a 2 digit number.")
elif int(time_list[0]) < 0 or int(time_list[0]) > 23:
    print("Hours must be between 0 and 23.")
elif int(time_list[1]) < 0 or int(time_list[1]) > 59:
    print("Minutes must be between 0 and 59.")
elif int(time_list[2]) < 0 or int(time_list[2]) > 59:
    print("Seconds must be between 0 and 59.")
else:
    time_output = ""
    for i in time_list:
        time_output += i
    print("Time with colons removed: ", time_output)
