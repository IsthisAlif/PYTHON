menu = {"Cheeseburger" : 3.50,
        "Chicken burger" : 4.00,
        "Double cheeseburger" : 5.00,
        "French fries" : 1.50,
        "Coca cola" : 1.50,
        "Drinking water" : 1.00}

def display_menu():
    for key, value in menu.items():
        print(f"{key}: RM{value:.2f}")

def display():
    print("_________________________________")
    print("Welcome to BurningHeat Restaurant")
    print("--------------MENU---------------")
    display_menu()
    print("_________________________________")
