# Personal Expense Analyzer & Budget Tracker

A web-based personal finance application for recording transactions, managing monthly budgets, and analyzing income and expenses through an interactive dashboard.

Built with **Python, Flask, PostgreSQL, SQLAlchemy, and Plotly**.

## Overview

The **Personal Expense Analyzer & Budget Tracker** is designed to help users keep track of their personal finances in a simple and organized way.

The application allows users to record income and expenses, categorize transactions, set monthly budgets, and monitor their financial activity through a dashboard. Financial records are stored in a PostgreSQL database and managed using SQLAlchemy.

The project was developed as a Python-based web application with a focus on practical database management, CRUD operations, data visualization, and user-friendly financial tracking.

## Features

### Transaction Management

Users can:

* Add income and expense transactions
* View recorded transactions
* Edit existing transactions
* Delete transactions
* Assign categories to transactions
* Record transaction dates
* Add descriptions and transaction amounts

### Interactive Dashboard

The dashboard provides a quick summary of financial activity, including:

* Total income
* Total expenses
* Current balance
* Number of transactions
* Expenses by category
* Income versus expenses

### Budget Tracking

Users can set and monitor a monthly spending budget.

The budget section displays:

* Monthly budget amount
* Total amount spent
* Remaining budget
* Budget usage percentage
* Visual budget progress

### Data Visualization

The application uses **Plotly** to present financial information visually.

Visualizations include:

* Expenses by category
* Income versus expenses
* Budget usage and progress

These visualizations make it easier to understand spending patterns and monitor financial performance.

## Technologies Used

### Backend

* **Python** – Main programming language
* **Flask** – Web application framework
* **SQLAlchemy** – Database ORM
* **Psycopg2** – PostgreSQL database adapter

### Database

* **PostgreSQL** – Stores transaction and budget information

### Frontend

* **HTML**
* **CSS**
* **JavaScript**

### Visualization

* **Plotly** – Interactive financial charts and graphs

### Configuration and Development

* **python-dotenv** – Environment variable management
* **Git** – Version control
* **GitHub** – Source code repository
* **uv** – Python project and dependency management

## Project Structure

```text
personal-expense-analyzer/
│
├── templates/
│   ├── add_transaction.html
│   ├── budget.html
│   ├── dashboard.html
│   ├── edit_transaction.html
│   └── transactions.html
│
├── .gitignore
├── app.py
├── database.py
├── pyproject.toml
├── requirements.txt
├── test_database.py
├── uv.lock
└── README.md
```

## Requirements

Before running the application, make sure the following are installed:

* Python 3.12 or later
* PostgreSQL
* Git

The required Python packages are listed in `requirements.txt`.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Bin-ita/personal-expense-analyzer.git
```

Move into the project directory:

```bash
cd personal-expense-analyzer
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create a PostgreSQL database for the application.

The application uses environment variables for database configuration. Create a `.env` file in the project directory and provide the required database connection details.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/expense_tracker
```

Replace the username, password, and database name with your own PostgreSQL configuration.

> **Note:** The `.env` file contains local configuration and should not be committed to GitHub.

## Running the Application

After completing the setup, start the Flask application:

```bash
python app.py
```

The application will start on the local development server.

Open the displayed local address in a web browser to access the application.

## Testing

The project includes database tests in:

```text
test_database.py
```

Run the tests using:

```bash
python -m pytest
```

If `pytest` is not installed, install it with:

```bash
pip install pytest
```

## Main Application Workflow

The application follows a simple workflow:

1. The user records an income or expense transaction.
2. Transaction information is stored in the PostgreSQL database.
3. Users can view, edit, or delete their transactions.
4. The dashboard retrieves stored data and calculates financial summaries.
5. Plotly visualizations present spending and income information.
6. Users can set a monthly budget and monitor their spending progress.

## Database

PostgreSQL is used as the primary database.

SQLAlchemy provides the database interaction layer, allowing the application to perform operations such as:

* Creating transaction records
* Reading stored transactions
* Updating existing records
* Deleting records
* Managing budget information

This provides a structured and reliable way to manage the application's financial data.

## Security and Configuration

Sensitive configuration values such as database credentials are stored using environment variables rather than being directly written into the application source code.

The `.gitignore` file prevents local environment files, virtual environments, Python cache files, and other unnecessary files from being uploaded to the repository.

## Future Improvements

Possible future improvements include:

* User authentication and multiple user accounts
* Exporting financial reports to CSV or PDF
* Advanced filtering by date and category
* Recurring transactions
* Savings goals
* More detailed spending analysis
* Improved mobile responsiveness
* Additional financial charts and reports

## Project Purpose

This project demonstrates the practical use of Python for developing a database-driven web application.

It combines:

* Python programming
* Flask web development
* CRUD operations
* Relational database management
* SQLAlchemy ORM
* Data visualization
* Environment configuration
* Automated testing
* Git and GitHub version control

## Author

**Binita Rimal**

**Personal Expense Analyzer & Budget Tracker**

