import json
import os
# Using while loop to create a menu driven program for expense management. The program should allow the user to add an expense, view all expenses, and calculate the total expenses. The expenses should be stored in a JSON file.
while True:
    print("Expense Management System")
    print("1. Add expense")
    print("2. View all expense")
    print("3. Total expense")
    print("0. Exit")

    choice  = input("Enter choice(1/2/3/4): ")

    if choice == "1":
        # Get user input for amount, category, and note
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").lower()
        note = input("Enter note: ").lower()
# Check if the expense.json file exists, if it does, read the existing expenses and append the new expense to the list. If it doesn't exist, create a new list and add the new expense to it. Finally, write the updated list back to the expense.json file.
        if os.path.exists("expense.json"):
            with open("expense.json", "r") as file:
                expense = json.load(file)
# Append the new expense to the list of expenses
                expense.append({"amount": amount, "category": category, "note": note})

            with open("expense.json", "w") as file:
                json.dump(expense, file, indent=4)
        else:
            expense = []
    elif choice == "2":
        with open("expense.json", "r")as file:
            expense = json.load(file)
        for item in expense:
         # Using the get method to retrieve the amount, category, and note for each expense item and print them in a formatted way.
         print(item.get("amount"), item.get("category"), item.get("note"))

    elif choice == "3":
        with open("expense.json", "r") as file:
            expense = json.load(file)

        total = 0

        for item in expense:
            total += item.get("amount", 0)

        print("Total expense:", total)
    elif choice == "0":
        print("Have a nice day!")
        break
    else:
        print("invalid option!")
     