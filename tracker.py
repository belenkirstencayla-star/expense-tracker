# Expense Tracker - Installment 3          Author: Belen, Kirsten Cayla R.

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
intax = input("Tax? (in %) ").strip()
budget = float(input("Budget? ").strip())


print("-" * 40)
print("SUMMARY")
print("-" * 40)

print("-".ljust(6) + f"{first_expense} - ${first_amount:.2f}")
print("-".ljust(6) + f"{second_expense} - ${second_amount:.2f}")

total = first_amount + second_amount
average = total / 2
tax = total * float(intax) / 100
Gtotal = total + tax


print(f"Subtotal = ${total:.2f}".rjust(10))
print(f"Average = ${average:.2f}".rjust(10))
print(f"Tax ({intax}.0%) = ${tax:.2f}".rjust(10))
print(f"Average = ${average:.2f}".rjust(10))
print(f"Grand total = ${Gtotal:.2f}".rjust(10))
print(f"Over Budget?: {'True'.rjust(10) if Gtotal > budget else 'False'.rjust(10)}")
print(f"Budget = ${budget:.2f}".rjust(10))

print("-" * 40)
print("Made by: Belen, Kirsten Cayla R. | Installment 2" )
print("")