print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
addPepperoni = input("Do you want pepperoni? Y or N ")
extraCheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if addPepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

if extraCheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
