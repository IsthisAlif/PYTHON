# Calculate circumference
import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
circumference = round(circumference, 2)

print(f"The circumference of the circle is: {circumference}cm")