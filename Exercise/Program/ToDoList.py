def display_ui():
    print("1. Add a task")
    print("2. View task")
    print("3. Remove a task")
    print("4. Exit the app")

def add_task(to_do_items):
    task = input("Enter the task: ")
    to_do_items.append(task)
    print(f"'{task}' added successfully")

def view_task(to_do_items):
    if len(to_do_items) == 0:
        print("No task available")
    else:
        print("Your task: ")
        for i, task in enumerate(to_do_items, start=1):
            print(f"{i}. {task}")

def remove_task(to_do_items):
    if len(to_do_items) == 0:
        print("No task available")
    else:
        print("Your task: ")
        for i, task in enumerate(to_do_items, start=1):
            print(f"{i}. {task}")

        try:
            i = int(input("Enter the task number you wanted to remove: "))-1
            if 0 <= i < len(to_do_items):
                remove = to_do_items.pop(i)
                print(f"Task '{remove}' has been removed")
            else:
                print("Invalid task")
        except ValueError:
            print("Invalid input")

def main():

    to_do_items = []
    is_running = True

    print("Welcome To Python To Do app")
    display_ui()

    while is_running:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(to_do_items)
        elif choice == '2':
            view_task(to_do_items)
        elif choice == '3':
            remove_task(to_do_items)
        elif choice == '4':
            print("Exiting the app...")
            is_running = False
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()