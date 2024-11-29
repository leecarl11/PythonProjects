weight=float(input("Enter your weight: "))
unit=input("Enter your unit: kilograms or pounds? (K or L): ")

if unit=="K":
    weight=weight*2.205
    unit="pounds"
    print(f"Your weight is {round(weight, 2)} {unit} ")
elif unit=="L":
    weight=weight/2.205
    unit="kilograms"
    print(f"Your weight is {round(weight, 2)} {unit} ")
else:
    print(f"{unit} is not a valid unit. ")
