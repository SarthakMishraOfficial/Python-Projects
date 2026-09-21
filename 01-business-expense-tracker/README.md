# Business Expense Tracker

## 1. Project Overview

The **Business Expense Tracker** is a command-line Python application designed to record, manage, and analyze expense data.

The project was developed as a practical application of Python fundamentals and is designed to demonstrate how basic programming concepts can be used to solve a real-world business problem.

The application allows users to record expenses, analyze spending patterns, manage a monthly budget, and generate basic financial insights.

---

## 2. Business Problem

Managing daily expenses manually can make it difficult to understand where money is being spent and whether spending is staying within a planned budget.

A simple expense-tracking system can help users:

- Record expenses systematically
- Calculate total spending
- Analyze daily and monthly expenses
- Identify the highest and lowest expenses
- Set a monthly budget
- Monitor budget usage
- Identify when spending exceeds the planned budget

This project demonstrates how Python can be used to build a basic business-oriented data management application.

---

## 3. Project Objectives

The main objectives of this project are:

- Build a practical Python application using fundamental concepts.
- Practice structured data storage using lists and dictionaries.
- Apply conditional logic and loops to process data.
- Use functions to organize application logic.
- Implement input validation and error handling.
- Perform basic expense analysis.
- Apply business logic to budget management.
- Create a portfolio-ready Python project.

---

## 4. Key Features

The application provides the following features:

## Add Expense

## View All Expenses ## Calculate Total Expense ## Daily Expense Analysis ## Monthly Expense Analysis ## Highest Expense Analysis ## Lowest Expense Analysis ## Set Monthly Budget ## Check Budget Status ## Calculate Remaining Budget ## Exit Application

---

## 5. Expense Categories

The application supports the following expense categories:

- Food
- Transport
- Education
- Shopping
- Entertainment
- Bills
- Healthcare
- Other

These categories allow expenses to be organized into meaningful business categories.

---

## 6. Expense Information

Each expense record contains four main fields:

- Date
- Category
- Description
- Amount

Example:

Date: **2026**-01-15 Category: Food Description: Lunch Amount: ₹**250**

---

## 7. Daily Expense Analysis

Users can enter a specific date to calculate the total amount spent on that day.

Example:

Date: **2026**-01-15

Daily Expense: ₹1,**250**

The program checks all available expense records and adds the amounts belonging to the selected date.

---

## 8. Monthly Expense Analysis

Users can enter a specific month to calculate the total amount spent during that month.

Example:

Month: **2026**-01

Monthly Expense: ₹12,**450**

This allows users to understand their monthly spending.

---

## 9. Highest Expense Analysis

The application identifies the expense with the highest amount.

Example:

Date: **2026**-02-15 Category: Shopping Description: Electronics Amount: ₹7,**500**

This helps identify the largest individual expense recorded.

---

## 10. Lowest Expense Analysis

The application identifies the expense with the lowest amount.

Example:

Date: **2026**-01-03 Category: Transport Description: Bus fare Amount: ₹20

This provides information about the smallest individual expense.

---

## 11. Monthly Budget Management

Users can define a monthly spending budget.

Example:

Monthly Budget: ₹20,**000**

The budget is then used to compare planned spending against actual monthly expenses.

---

## 12. Budget Status

The application compares monthly expenses with the defined monthly budget.

There are three possible results:

### Under Budget

Monthly expenses are less than the budget.

Example:

Monthly Budget: ₹20,**000** Monthly Expense: ₹15,**000**

Status: Under Budget

### Budget Fully Used

Monthly expenses are equal to the budget.

Example:

Monthly Budget: ₹20,**000** Monthly Expense: ₹20,**000**

Status: Budget Fully Used

### Over Budget

Monthly expenses are greater than the budget.

Example:

Monthly Budget: ₹20,**000** Monthly Expense: ₹23,**000**

Status: Over Budget

---

## 13. Remaining Budget

The application calculates the amount remaining from the monthly budget.

Formula:

Remaining Budget = Monthly Budget − Monthly Expense

Example:

Monthly Budget: ₹20,**000** Monthly Expense: ₹15,**500**

Remaining Budget: ₹4,**500**

If expenses exceed the budget, the application displays the amount by which the budget has been exceeded.

---

## 14. Python Concepts Used

This project applies the following Python concepts:

### Python Fundamentals

- Variables
- Constants
- Data Types
- Type Conversion
- Input and Output
- Operators

### Control Flow

- if
- elif
- else
- for loops
- while loops
- break
- continue

### Data Structures

- Lists
- Dictionaries

### Functions

- Function definition
- Function calls
- Parameters
- Arguments
- Return values

### Error Handling

- try
- except
- ValueError

### String Operations

- String comparison
- startswith()
- strip()
- String formatting

### Program Structure

- main()
- if **name** == ***main***

---

## 15. Input Validation

The application includes validation to prevent incorrect data from entering the system.

Validation includes:

- Menu option validation
- Expense amount validation
- Category validation
- Description validation
- Date format validation
- Monthly budget validation
- Numeric input validation

For example, expense amounts must be greater than zero.

Invalid numeric input is handled using exception handling.

---

## 16. Sample Dataset

A synthetic dataset containing ****500** expense records** was created for testing and demonstration.

The dataset covers:

- January **2026**
- February **2026**
- March **2026**

The dataset contains:

- Date
- Category
- Description
- Amount

The dataset is stored at:

data/sample_expenses.csv

The data is synthetically generated and does not contain private financial information.

---

## 17. Project Structure

01-business-expense-tracker/

**README**.md

expense_tracker.py

generate_sample_data.py

data/

sample_expenses.csv

screenshots/

documentation/

project_plan.md

---

## 18. Application Flow

The application follows a menu-driven architecture.

### Start Application

↓

### Initialize Data

↓

### Display Main Menu

↓

User Selects an Option

↓

### Perform Selected Operation

↓

### Display Result

↓

Return to Main Menu

↓

### User Selects Exit

↓

### End Application

---

## 19. Application Architecture

The application is divided into separate functions based on their responsibilities.

Major functions include:

- add_expense()
- view_expenses()
- calculate_total()
- calculate_daily_expense()
- calculate_monthly_expense()
- find_highest_expense()
- find_lowest_expense()
- set_monthly_budget()
- check_budget_status()
- calculate_remaining_budget()
- main()

This structure makes the program easier to understand, test, maintain, and extend.

---

## 20. Data Structure

Each expense is represented using a Python dictionary.

Example:

Date: **2026**-01-15 Category: Food Description: Lunch Amount: ₹**250**

Multiple expense records are stored inside a Python list.

This structure allows the application to process multiple expense records using loops and functions.

---

## 21. Testing

The application was tested using both valid and invalid inputs.

### Functional Testing

Tested:

- Adding expenses
- Viewing expenses
- Calculating total expenses
- Daily expense analysis
- Monthly expense analysis
- Highest expense
- Lowest expense
- Setting monthly budget
- Checking budget status
- Calculating remaining budget
- Exiting the application

### Validation Testing

Tested:

- Invalid menu options
- Negative amounts
- Zero amounts
- Non-numeric amounts
- Invalid categories
- Empty descriptions
- Invalid dates
- Invalid budgets
- Empty expense list
- Budget not set

### Budget Testing

All three budget conditions were tested:

- Monthly Expense < Budget
- Monthly Expense = Budget
- Monthly Expense > Budget

---

## 22. Current Limitations

The current version intentionally focuses on Python fundamentals.

Current limitations include:

- Data entered manually is stored only while the application is running.
- Manually entered data is lost when the program closes.
- The **CSV** dataset is currently used as sample data.
- The application does not yet use a database.
- No graphical user interface is implemented.
- No data visualization is implemented.
- No external Python libraries are required.

These limitations provide opportunities for future development.

---

## 23. Future Improvements

Future versions of the project can include:

- **CSV** data import
- **CSV** data export
- Persistent data storage
- SQLite database
- Search functionality
- Expense filtering
- Category-wise analysis
- Monthly comparison
- Spending trends
- Pandas-based analysis
- Matplotlib visualizations
- Dashboard development
- Automated reports
- **GUI** application
- Web application
- AI-powered spending insights

---

## 24. Business Analytics Relevance

Although this project is built using Python fundamentals, it introduces several concepts relevant to Business Analytics.

### Data Collection

Collecting structured expense information.

### Data Validation

Ensuring that incorrect information does not enter the system.

### Data Processing

Processing multiple expense records to calculate business metrics.

### Data Segmentation

Analyzing expenses based on:

- Date
- Month
- Category

### KPI Calculation

The application calculates basic financial metrics such as:

- Total Expense
- Daily Expense
- Monthly Expense
- Highest Expense
- Lowest Expense
- Remaining Budget

### Decision Support

Budget analysis provides information that can help users understand whether their spending is within the planned budget.

---

## 25. Learning Outcomes

By completing this project, the following skills were practiced:

- Building a complete Python **CLI** application
- Working with lists and dictionaries
- Using loops for data processing
- Writing reusable functions
- Passing data between functions
- Using return values
- Handling invalid user input
- Applying business rules
- Structuring a Python project
- Testing application functionality
- Generating synthetic datasets
- Preparing a project for GitHub

---

## 26. Technologies Used

### Programming Language

Python

### Development Environment

### Visual Studio Code

### Data Format

**CSV**

### Version Control

Git and GitHub

---

## 27. Project Development Approach

The project was developed progressively.

### Phase 1 — Python Fundamentals

Learned and practiced:

- Variables
- Data Types
- Operators
- Input and Output
- Conditional Statements
- Loops

### Phase 2 — Application Planning

Defined:

- Features
- Business requirements
- Data structure
- Menu structure
- Validation requirements

### Phase 3 — Core Application

Implemented:

- Main menu
- Expense management
- Expense calculations
- Budget management
- Input validation

### Phase 4 — Functions and Program Structure

Refactored the application using:

- Functions
- Parameters
- Arguments
- Return values
- main()
- Program entry point

### Phase 5 — Testing Dataset

Created a synthetic dataset containing **500** expense records covering January to March **2026**.

---

## 28. Project Status

Current project status:

Python Fundamentals — Completed

Core Application — Completed

Input Validation — Completed

Functions — Completed

Error Handling — Completed

Main Function — Completed

Testing — Completed

Sample Dataset — Completed

**README** Documentation — Completed

Project Plan — Completed

The current version represents a completed Python fundamentals project.

---

## 29. Future Development Roadmap

The project can gradually evolve from a basic Python application into a more advanced analytics project.

### Python Fundamentals

↓

### File Handling

↓

**CSV** Integration

↓

Pandas

↓

### Data Cleaning

↓

### Data Analysis

↓

### Data Visualization

↓

**SQL** Database

↓

### Business Analytics

↓

Dashboard

↓

### Advanced Analytics

This progression will allow the project to demonstrate the transition from Python programming fundamentals to practical data and business analytics.

---

## 30. Author

### Sarthak Mishra

**BBA** Student | Business Analytics & AI Enthusiast

Areas of Interest:

- Business Analytics
- Data Analytics
- Python
- **SQL**
- Excel
- Artificial Intelligence
- Product Analytics

---

## 31. License

This project is created for educational, learning, and portfolio purposes.

The project will be continuously improved as new Python programming, data analysis, database, and business analytics concepts are learned.