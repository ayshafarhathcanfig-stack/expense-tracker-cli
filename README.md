# Expense Tracker CLI

A simple command-line application to track daily expenses using Python and SQLite.


## What the Program Does

This program helps you manage your personal expenses from the terminal.
You can add new expenses, view all expenses, search by category, and delete expenses.
All data is saved automatically in a local database file called `expenses.db`.


## How to Run

1. Make sure Python is installed on your computer
2. Download or clone this project
3. Open a terminal in the project folder
4. Run the program using this command:

python main.py

5. The menu will appear — choose an option by typing 1, 2, 3, 4, or 5

---

## Features Implemented

1. Add Expense
   - Enter title, amount, and category
   - Date is saved automatically as today's date

2. View All Expenses
   - Displays all saved expenses in a table
   - Shows ID, title, amount, category, and date

3. Search by Category
   - Search expenses by typing a category name
   - Example: type "Food" to see all food expenses

4. Delete Expense
   - View all expenses first
   - Enter the ID number of the expense to delete

5. Exit
   - Closes the program safely



## Database

- Database file : expenses.db
- Table name    : expenses
- Columns       : id, title, amount, category, date

---

## Project Structure

expense-tracker-cli/
├── main.py        → main program file
├── expenses.db    → database 
└── README.md      → project documentation


Your project folder should now look like this:
expense-tracker-cli/
├── main.py
├── expenses.db
└── README.md