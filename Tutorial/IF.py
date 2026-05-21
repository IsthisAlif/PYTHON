# if = Do some code only if some condition is true
#      Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("Your are now signed up!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You must be 18+ to sign up.")


response = input("Would you like food? (Y/N)")

if response == "Y":
    print("Here is some food!")
else:
    print("No food for you then!")

name = input("Enter your name:")

if name == "":
    print("You did not enter a name!")
else:
    print(f"Hello {name}!")

for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")