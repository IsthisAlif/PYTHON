from menu import *

def main():

    total = 0
    is_running = True

    display()

    while is_running:
        order = input("What do you want to order?(q to checkout): ").lower().capitalize()

        if order in menu:
            amount = int(input("How many do you want: "))
            print(f"You have ordered {amount} {order}")
            total += amount * menu[order]
            print(f"Current total : RM{total:.2f}")
            continue
        elif order == 'Q':
            print("_________________________________")
            print(f"Thank you, your final total is RM{total:.2f}")
            print("---------------------------------")
            is_running = False
        else:
            print("Invalid Order")
            continue

if __name__ == '__main__':
    main()