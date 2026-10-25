# Week 2 Assignment: Contact Book & Task Manager
# A simple menu-driven program using lists, dictionaries, and functions.

contacts = []
tasks = []


def get_non_empty_input(message):
    """Ask for input until the user enters something."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


def add_contact():
    name = get_non_empty_input("Enter name: ")
    phone = get_non_empty_input("Enter phone number: ")
    email = get_non_empty_input("Enter email: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return

    print("\n--- Contacts ---")
    for number, contact in enumerate(contacts, start=1):
        print(f"{number}. {contact['name']} | {contact['phone']} | {contact['email']}")


def update_contact():
    view_contacts()
    if not contacts:
        return

    try:
        number = int(input("Enter the contact number to update: "))
        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    contact = contacts[number - 1]
    name = input(f"Name ({contact['name']}): ").strip()
    phone = input(f"Phone ({contact['phone']}): ").strip()
    email = input(f"Email ({contact['email']}): ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    view_contacts()
    if not contacts:
        return

    try:
        number = int(input("Enter the contact number to delete: "))
        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed = contacts.pop(number - 1)
    print(f"{removed['name']} was deleted.")


def add_task():
    title = get_non_empty_input("Enter task: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks saved.")
        return

    print("\n--- Tasks ---")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{number}. {task['title']} - {status}")


def update_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter the task number to update: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    new_title = input("Enter the new task name (or press Enter to keep it): ").strip()
    if new_title:
        tasks[number - 1]["title"] = new_title

    answer = input("Is the task completed? (y/n): ").strip().lower()
    if answer == "y":
        tasks[number - 1]["completed"] = True
    elif answer == "n":
        tasks[number - 1]["completed"] = False

    print("Task updated successfully.")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter the task number to delete: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed = tasks.pop(number - 1)
    print(f"Task '{removed['title']}' was deleted.")


def main():
    """Display the main menu and run the program."""
    while True:
        print("\n=== Contact Book & Task Manager ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Add task")
        print("6. View tasks")
        print("7. Update task")
        print("8. Delete task")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            add_task()
        elif choice == "6":
            view_tasks()
        elif choice == "7":
            update_task()
        elif choice == "8":
            delete_task()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
