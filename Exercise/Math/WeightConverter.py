# Weight converter program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K/P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "LBS"
elif unit == "P":
    weight = weight / 2.205
    unit = "KGS"
else:
    print("Invalid unit!")

print(f"Your weight is {round(weight, 2)} {unit}")