import json
import os
# Using a while loop to keep the program running
while True:
    # User homepage
    print("menu")
    print("1. Add expenses")
    print("2. View all expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = input("choose an option (1/2/3/4): ")
    if choice == "1":
        # declaring my variables
        amount = int(input("Enter amount: "))
        category = input("Enter category: ").lower()
        note = input("Enter note: ").lower()
# using json read,write and append
        if os.path.exists("expense.json"):
            with open("expense.json", "r") as file:
                expense = json.load(file)

            expense.append({"amount": amount, "category": category, "note":note})

            with open("expense.json", "w") as file:
                json.dump(expense, file, indent=4)
        else:
            expense = []
        

    elif choice == "2":
        file = open("expense.json", "r")
        expense = json.load(file)
        # using for loop
        for item in expense:
            print(item["amount"], item["category"], item["note"])
        file.close()

    elif choice == "3":
        file = open("expense.json", "r")
        expense = json.load(file)
        file.close()

        total = 0

        for item in expense:
            total += item.get("amount", 0)

        print("Total expense:", total)
        file.close()

    elif choice == "4":
        print("thank you for using this app thank you")
        break
    else:
        print("invalid option")