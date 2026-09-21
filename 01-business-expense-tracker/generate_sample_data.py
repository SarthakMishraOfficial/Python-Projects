import csv
import random
from datetime import date, timedelta


categories = {
    "Food": [
        "Breakfast",
        "Lunch",
        "Dinner",
        "Snacks",
        "College canteen",
        "Restaurant"
    ],

    "Transport": [
        "Bus fare",
        "Auto fare",
        "Cab",
        "Fuel",
        "Metro",
        "Parking"
    ],

    "Education": [
        "Books",
        "Notebook",
        "Python course",
        "Stationery",
        "Printing",
        "Exam fee"
    ],

    "Shopping": [
        "Clothes",
        "Shoes",
        "Electronics",
        "Accessories",
        "Personal items"
    ],

    "Entertainment": [
        "Movie",
        "Gaming",
        "Streaming subscription",
        "Event",
        "Cafe"
    ],

    "Bills": [
        "Mobile recharge",
        "Internet bill",
        "Electricity bill",
        "Subscription"
    ],

    "Healthcare": [
        "Medicine",
        "Doctor consultation",
        "Medical test"
    ],

    "Other": [
        "Gift",
        "Donation",
        "Miscellaneous",
        "Unexpected expense"
    ]
}


amount_ranges = {
    "Food": (50, 1500),
    "Transport": (20, 2000),
    "Education": (100, 5000),
    "Shopping": (100, 8000),
    "Entertainment": (100, 3000),
    "Bills": (100, 5000),
    "Healthcare": (100, 5000),
    "Other": (50, 5000)
}


start_date = date(2026, 1, 1)
end_date = date(2026, 3, 31)


number_of_records = 500


expenses = []


for i in range(number_of_records):

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    expense_date = start_date + timedelta(days=random_days)

    category = random.choice(list(categories.keys()))

    description = random.choice(categories[category])

    minimum, maximum = amount_ranges[category]

    amount = random.randint(minimum, maximum)

    expense = {
        "date": expense_date.strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)


expenses.sort(key=lambda expense: expense["date"])


with open("data/sample_expenses.csv", "w", newline="") as file:

    fieldnames = [
        "date",
        "category",
        "description",
        "amount"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(expenses)


print("Sample data generated successfully.")
print("Total records:", len(expenses))
print("CSV file created successfully.")
print("Location: data/sample_expenses.csv")