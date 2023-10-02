height = float(input("What is your height in m? "))
weight = float(input("What is your weight in km? "))
bmi = weight / (height * height)
bmi2 = round(bmi, 2)
if bmi < 18.5:
    print(f"This is your bmi:",bmi2, "You are underweight")
elif bmi <= 25:
    print(f"This is your bmi:",bmi2, "You have normal weight")
elif bmi <= 30:
    print(f"This is your bmi:",bmi2, "You are slightly overweight")
elif bmi <= 35:
    print(f"This is your bmi:",bmi2, "You are obese")
else:
    print(f"This is your bmi:",bmi2, "You are clinically obese")
