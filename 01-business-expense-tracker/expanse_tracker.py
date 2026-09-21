
print("========================================")
print("       BUSINESS EXPENSE TRACKER")
print("========================================")
print("Project successfully started!")


# =========================================================
# 1. ADD EXPENSE
# =========================================================

def add_expense(expenses, categories):

    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            break
        else:
            print("Please enter date in YYYY-MM-DD format.")

    while True:
        print("\nAvailable Categories:")

        for category in categories:
            print("-", category)

        category = input("Enter category: ")

        if category in categories:
            break
        else:
            print("Invalid category. Please choose from the available categories.")

    while True:
        description = input("Enter description: ")

        if description.strip() != "":
            break
        else:
            print("Description cannot be empty.")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully.")


# =========================================================
# 2. VIEW ALL EXPENSES
# =========================================================

def view_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses recorded yet.")

    else:
        print("\n========== ALL EXPENSES ==========")

        for expense in expenses:
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount: ₹", expense["amount"])
            print("----------------------------------")


# =========================================================
# 3. CALCULATE TOTAL EXPENSE
# =========================================================

def calculate_total(expenses):

    total_expense = 0

    for expense in expenses:
        total_expense = total_expense + expense["amount"]

    return total_expense


# =========================================================
# 4. CALCULATE DAILY EXPENSE
# =========================================================

def calculate_daily_expense(expenses):

    selected_date = input("Enter date (YYYY-MM-DD): ")

    daily_expense = 0

    for expense in expenses:

        if expense["date"] == selected_date:
            daily_expense = daily_expense + expense["amount"]

    return daily_expense


# =========================================================
# 5. CALCULATE MONTHLY EXPENSE
# =========================================================

def calculate_monthly_expense(expenses):

    selected_month = input("Enter month (YYYY-MM): ")

    monthly_expense = 0

    for expense in expenses:

        if expense["date"].startswith(selected_month):
            monthly_expense = monthly_expense + expense["amount"]

    return monthly_expense


# =========================================================
# 6. FIND HIGHEST EXPENSE
# =========================================================

def find_highest_expense(expenses):

    if len(expenses) == 0:
        return None

    highest_expense = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest_expense["amount"]:
            highest_expense = expense

    return highest_expense


# =========================================================
# 7. FIND LOWEST EXPENSE
# =========================================================

def find_lowest_expense(expenses):

    if len(expenses) == 0:
        return None

    lowest_expense = expenses[0]

    for expense in expenses:

        if expense["amount"] < lowest_expense["amount"]:
            lowest_expense = expense

    return lowest_expense


# =========================================================
# 8. SET MONTHLY BUDGET
# =========================================================

def set_monthly_budget():

    while True:

        try:
            budget = float(input("Enter your monthly budget: "))

            if budget > 0:
                return budget

            else:
                print("Budget must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


# =========================================================
# 9. CHECK BUDGET STATUS
# =========================================================

def check_budget_status(expenses, monthly_budget):

    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return

    monthly_expense = calculate_monthly_expense(expenses)

    if monthly_expense < monthly_budget:

        print("Status: Under Budget")

    elif monthly_expense == monthly_budget:

        print("Status: Budget Fully Used")

    else:

        print("Status: Over Budget")


# =========================================================
# 10. CALCULATE REMAINING BUDGET
# =========================================================

def calculate_remaining_budget(expenses, monthly_budget):

    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return

    monthly_expense = calculate_monthly_expense(expenses)

    remaining_budget = monthly_budget - monthly_expense

    if remaining_budget > 0:

        print("Remaining Budget: ₹", remaining_budget)

    elif remaining_budget == 0:

        print("You have used your entire budget.")

    else:

        print("Budget Exceeded by: ₹", abs(remaining_budget))


# =========================================================
# 11. MAIN FUNCTION
# =========================================================

def main():

    # -----------------------------------------
    # PROGRAM DATA
    # -----------------------------------------

    expenses = []

    categories = [
        "Food",
        "Transport",
        "Education",
        "Shopping",
        "Entertainment",
        "Bills",
        "Healthcare",
        "Other"
    ]

    monthly_budget = 0


    # -----------------------------------------
    # MAIN MENU
    # -----------------------------------------

    while True:

        print("\n========================================")
        print("       BUSINESS EXPENSE TRACKER")
        print("========================================")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expense")
        print("4. Daily Expense")
        print("5. Monthly Expense")
        print("6. Highest Expense")
        print("7. Lowest Expense")
        print("8. Set Monthly Budget")
        print("9. Check Budget Status")
        print("10. Remaining Budget")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice (1-11): "))

        except ValueError:
            print("Please enter a number between 1 and 11.")
            continue


        # -----------------------------------------
        # OPTION 1
        # -----------------------------------------

        if choice == 1:

            add_expense(expenses, categories)


        # -----------------------------------------
        # OPTION 2
        # -----------------------------------------

        elif choice == 2:

            view_expenses(expenses)


        # -----------------------------------------
        # OPTION 3
        # -----------------------------------------

        elif choice == 3:

            total_expense = calculate_total(expenses)

            print("Total Expense: ₹", total_expense)


        # -----------------------------------------
        # OPTION 4
        # -----------------------------------------

        elif choice == 4:

            daily_expense = calculate_daily_expense(expenses)

            print("Daily Expense: ₹", daily_expense)


        # -----------------------------------------
        # OPTION 5
        # -----------------------------------------

        elif choice == 5:

            monthly_expense = calculate_monthly_expense(expenses)

            print("Monthly Expense: ₹", monthly_expense)


        # -----------------------------------------
        # OPTION 6
        # -----------------------------------------

        elif choice == 6:

            highest_expense = find_highest_expense(expenses)

            if highest_expense is None:

                print("No expenses recorded yet.")

            else:

                print("\n========== HIGHEST EXPENSE ==========")
                print("Date:", highest_expense["date"])
                print("Category:", highest_expense["category"])
                print("Description:", highest_expense["description"])
                print("Amount: ₹", highest_expense["amount"])


        # -----------------------------------------
        # OPTION 7
        # -----------------------------------------

        elif choice == 7:

            lowest_expense = find_lowest_expense(expenses)

            if lowest_expense is None:

                print("No expenses recorded yet.")

            else:

                print("\n========== LOWEST EXPENSE ==========")
                print("Date:", lowest_expense["date"])
                print("Category:", lowest_expense["category"])
                print("Description:", lowest_expense["description"])
                print("Amount: ₹", lowest_expense["amount"])


        # -----------------------------------------
        # OPTION 8
        # -----------------------------------------

        elif choice == 8:

            monthly_budget = set_monthly_budget()

            print("Monthly budget set successfully.")
            print("Your monthly budget is: ₹", monthly_budget)


        # -----------------------------------------
        # OPTION 9
        # -----------------------------------------

        elif choice == 9:

            check_budget_status(
                expenses,
                monthly_budget
            )


        # -----------------------------------------
        # OPTION 10
        # -----------------------------------------

        elif choice == 10:

            calculate_remaining_budget(
                expenses,
                monthly_budget
            )


        # -----------------------------------------
        # OPTION 11
        # -----------------------------------------

        elif choice == 11:

            print("Thank you for using Business Expense Tracker.")

            break


        # -----------------------------------------
        # INVALID OPTION
        # -----------------------------------------

        else:

            print("Invalid choice. Please select 1-11.")


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":

    main()