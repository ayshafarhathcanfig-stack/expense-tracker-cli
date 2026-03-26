import sqlite3
from datetime import date

# Connect to database
conn = sqlite3.connect("expenses.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        category TEXT,
        date TEXT
    )
""")
conn.commit()

def add_expense():
    title = input("Enter title: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    today = str(date.today())
    conn.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
                 (title, amount, category, today))
    conn.commit()
    print("Expense added!")

def view_expenses():
    rows = conn.execute("SELECT * FROM expenses").fetchall()
    if not rows:
        print("No expenses found.")
    else:
        print("\nID | Title | Amount | Category | Date")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

def search_expense():
    category = input("Enter category to search: ")
    rows = conn.execute("SELECT * FROM expenses WHERE category = ?", (category,)).fetchall()
    if not rows:
        print("No expenses found.")
    else:
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

def delete_expense():
    view_expenses()
    id = input("Enter ID to delete: ")
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    print("Expense deleted!")

# Main menu
while True:
    print("\n Expense Tracker ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")