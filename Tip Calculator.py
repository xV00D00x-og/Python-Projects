#!/usr/bin/env python 3
# A Simple tip calculator that rounds to two decimal places

print("Welcome to the tip calculator.")
total = (float(input("What was the total bill? ")))
tip = (float(input("What percentage tip would you like to give? 10, 12, 15, etc? ")))
people_count = (int(input("How many people will split the bill? ")))
tip_percentage = float(tip / 100 * total)
total_calculation = (total + tip_percentage) / people_count
pay = round(total_calculation, 2)
if people_count == 1:
    print("You should pay: ", pay)
else:
    print("Each person should pay: ", pay)
