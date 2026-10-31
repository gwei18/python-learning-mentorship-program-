

import csv

FILE_NAME = "expenses.csv"


def get_amount():
    """Gets a valid expense amount from the user."""
    while True:
        try:
            amount = float(input("Enter amount: ₦"))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def add_expense(expenses):
    """Adds a new expense to the list."""
    date = input("Enter date (DD/MM/YYYY): ").strip()
    category = input("Enter category (e.g. Food, Transport): ").strip()

    if date == "" or category == "":
        print("Date and category cannot be empty.")
        return

    amount = get_amount()

    expense = {
        "date": date,
        "category": category.title(),
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expenses):
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'No.':<5}{'Date':<15}{'Category':<20}{'Amount':>12}")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<20}"
            f"₦{expense['amount']:>10,.2f}"
        )


def spending_summary(expenses):
    """Shows total spending for each category."""
    if not expenses:
        print("No expenses available for a summary.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\n--- SPENDING SUMMARY ---")
    total = 0

    for category, amount in categories.items():
        print(f"{category}: ₦{amount:,.2f}")
        total += amount

    print(f"\nTotal spending: ₦{total:,.2f}")


def save_expenses(expenses):
    """Saves expenses to a CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "category", "amount"]
            )
            writer.writeheader()
            writer.writerows(expenses)

        print("Expenses saved successfully.")

    except OSError as error:
        print(f"Could not save the file: {error}")


def load_expenses():
    """Loads saved expenses from the CSV file."""
    expenses = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

        print("Previous expenses loaded.")

    except FileNotFoundError:
        print("No previous expense file found. Starting a new tracker.")

    except (OSError, ValueError) as error:
        print(f"Could not load expenses: {error}")

    return expenses


def main():
    """Runs the Personal Expense Tracker."""
    expenses = load_expenses()

    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View spending summary")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            spending_summary(expenses)

        elif choice == "4":
            save_expenses(expenses)

        elif choice == "5":
            save_expenses(expenses)
            print("Your expenses have been saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
