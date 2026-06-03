# Hypotenuse of triangle
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
hypotenuse = round(hypotenuse, 2)

print(f"The length of the hypotenuse is: {hypotenuse}cm")