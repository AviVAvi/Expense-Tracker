📘 Expense Tracker (Python Project)

A simple, menu-driven Expense Tracker built using Python, designed to help users record expenses, view spending history, and calculate total expenses.
This project demonstrates:

File handling

OOP (Object-Oriented Programming)

Input validation

Error handling

Data loading + serialization

Menu-based application flow

Perfect as an early portfolio project!


🚀 Features

✅ Add New Expense

Each expense includes:

Amount

Category

Note

Date (auto-added)

✅ View All Expenses

Prints each saved expense in a clean format.

✅ Calculate Total Spent

Loads all expenses and shows the sum of all recorded amounts.

✅ Safe Input Handling

Prevents crashes using:

integer/float validation

try/except blocks

skipped corrupt lines

✅ Persistent Storage

All expenses are saved in a simple text file:

expenses.txt


Each line looks like:

50.0;Food;Pizza;2025-02-23


🛠️ Tech Used

Python 3

OOP

File Handling

Error Handling

datetime module


📂 Project Structure

expense-tracker/

│

├── expense_tracker.py      # main program

├── expenses.txt            # created automatically when expenses are added

└── README.md               # project documentation


▶️ How to Run

Clone the project:

git clone https://github.com/yourusername/expense-tracker.git


Open the folder:

cd expense-tracker


Run the Python file:

python expense_tracker.py


📝 Sample Output

-----Expense Tracker-----
1: Add Expense
2: Show All Expenses
3: Show Total Spent
4: Exit

Choose an option (1-4): 1
Enter Amount: 50
Enter Category: Food
Enter Note: Pizza
Expense saved!


⭐ Future Upgrades (Planned)

This project will later evolve into a full Personal Finance Manager as part of my major projects roadmap.
Planned features include:

Category totals

Monthly reports

Data visualizations

CSV export

SQLite database backend

Budget alerts

GUI dashboard

These upgrades will happen later as I advance in Python.

👤 Author

Asmit
