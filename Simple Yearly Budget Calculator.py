print("Please enter the amount spent in each month of last year")
Spending = float(input("Enter amount spent in Jan: "))
Spending1 = float(input("Enter amount spent in Feb: "))
Spending2 = float(input("Enter amount spent in Mar: "))
Spending3 = float(input("Enter amount spent in Apr: "))
Spending4 = float(input("Enter amount spent in May: "))
Spending5 = float(input("Enter amount spent in Jun: "))
Spending6 = float(input("Enter amount spent in Jul: "))
Spending7 = float(input("Enter amount spent in Aug: "))
Spending8 = float(input("Enter amount spent in Sep: "))
Spending9 = float(input("Enter amount spent in Oct: "))
Spending10 = float(input("Enter amount spent in Nov: "))
Spending11 = float(input("Enter amount spent in Dec: "))

expenditures_list = [Spending, Spending1, Spending2, Spending3, Spending4, Spending5, Spending6, Spending7, Spending8, Spending9, Spending10, Spending11]

low = 0.0
normal = 0.0
high = 0.0
for amount in expenditures_list:
    if amount <= 1000.0:
        low += 1
    elif amount <= 2500.0:
        normal += 1
    else:
        high += 1

print("Numbers of months with low spending: ", str(low), "\nNormal spending: ", str(normal), "\nHigh spending: ", str(high))
