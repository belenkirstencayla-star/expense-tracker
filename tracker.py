# Expense Tracker - Installment 2          Author: Belen, Kirsten Cayla R.

print("")
print("")
print("=" * 40)
print("EXPENSE TRACKER" .center(40))
print("Know where your money goes" .center(40))
print("=" * 40)

name = input("What's your name? ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

print("MAIN MENU")
print("[1] Add Expense" .ljust(35) + "(coming soon)")
print("[2] View Expenses" .ljust(35) + "(coming soon)")
print("[3] View Summary" .ljust(35) + "(coming soon)")
print("[4] Exit" .ljust(35) + "(coming soon)")
print("")


first_expense = input("First Expense? ").strip()
first_amount = float(input("Amount? "))

second_expense = input("Second Expense? ").strip()
second_amount = float(input("Amount? "))

print("-" * 40)

print("SUMMARY")

print("-".ljust(6) + f"{first_expense} - ${first_amount:.2f}")
print("-".ljust(6) + f"{second_expense} - ${second_amount:.2f}")

total = first_amount + second_amount
average = total / 2

print(f"Total Spent = ${total:.2f}")
print(f"Average = ${average:.2f}")

print("-" * 40)
print("Made by: Belen, Kirsten Cayla R. | Installment 2" )
print("")