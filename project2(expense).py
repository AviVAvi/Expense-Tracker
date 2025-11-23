import datetime


class Expense:
    def __init__(self, amount, category, note, date=None):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date if date else datetime.date.today()

    def save(self):
        with open("expenses.txt", "a") as file:
            file.write(f"{self.amount};{self.category};{self.note};{self.date}\n")

    def show(self):
        print(f"Amount: {self.amount} | Category: {self.category} | Note: {self.note} | Date: {self.date}")


def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                try:
                    amount_str, category, note, date_str = line.strip().split(";")
                    amount = float(amount_str)
                    date = datetime.date.fromisoformat(date_str)
                    exp = Expense(amount, category, note, date)
                    expenses.append(exp)

                except ValueError:
                    print("Skipping line: ", line.strip())
                    continue

    except FileNotFoundError:
        print("No expense data yet.")
    return expenses


def get_valid_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Enter valid number!")


def get_valid_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Enter valid number!")


def show_menu():
    print("-----Expense Tracker-----")
    print("1: Add Expense")
    print("2: Show All Expenses")
    print("3: Show Total Spent")
    print("4: Exit\n")


def main():
    expenses=[]
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            amount=get_valid_float("Enter Amount: ")
            category=input("Enter Category: ")
            note=input("Enter Note: ")
            exp=Expense(amount, category, note)
            exp.save()

        elif choice == "2":
            expenses=load_expenses()
            for e in expenses:
                e.show()


        elif choice == "3":
            total=0
            expenses = load_expenses()
            for e in expenses:
                total+=e.amount
            print(f"Total spent: {total:.2f}\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

