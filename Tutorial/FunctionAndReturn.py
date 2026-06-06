# function = A block of reusable code
#            place () after the function name to invoke it

# 1
def happy_birthday(name, age):
    print(f"Happy Birthday {name}!")
    print(f"Happy Birthday to {name}!")
    print("Happy Birthday dear friend")
    print(f"Happy Birthday to {name}!")
    print(f"Congratulations {name}! You are now {age}.")
    print()

name = input("What is your name? ")
age = int(input("How old are you? "))

happy_birthday(name, age)

# 2
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date} ")
    print()

display_invoice("Bro", 42.50, "01/01/2026")

# return = statement used to end a function
#          and send a result back to the caller

# 3
def add(x, y):
    z = x + y 
    return z

def subtract(x, y):
    z = x - y 
    return z

def multiply(x, y):
    z = x * y 
    return z

def divide(x, y):
    z = x / y 
    return z

print(add(5, 10))
print(subtract(5, 10))
print(multiply(5, 10))
print(divide(5, 10))
print()

# 4
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")
print(full_name)
