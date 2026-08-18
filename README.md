# Personal Expense Analyzer & Budget Tracker

A simple web-based application for managing personal income, expenses, and monthly budgets.

Built using Python, Flask, PostgreSQL, SQLAlchemy, and Plotly.

## Overview

Personal Expense Analyzer & Budget Tracker helps users manage their daily financial transactions and monitor their spending.

Users can add, view, edit, and delete transactions, set monthly budgets, and analyze their financial information through an interactive dashboard.

The application uses PostgreSQL to store financial data and SQLAlchemy to handle database operations.

## Features

### Transaction Management

- Add income and expense transactions
- View all recorded transactions
- Edit existing transactions
- Delete transactions
- Categorize transactions
- Store transaction dates, descriptions, and amounts

### Dashboard

The dashboard provides an overview of:

- Total income
- Total expenses
- Current balance
- Number of transactions
- Expenses by category
- Income versus expenses

### Budget Tracking

Users can set a monthly spending budget and monitor their progress.

The system displays:

- Monthly budget
- Amount spent
- Remaining budget
- Budget usage percentage
- Budget progress bar

### Data Visualization

Plotly is used to provide visual representations of financial data, including:

- Expenses by category
- Income versus expenses
- Budget usage

## Technologies Used

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Plotly
- HTML
- CSS
- JavaScript
- python-dotenv
- Git
- GitHub

## Project Structure

```text
Expense Tracker/
│
├── templates/
│   ├── add_transaction.html
│   ├── budget.html
│   ├── dashboard.html
│   ├── edit_transaction.html
│   └── transactions.html
│
├── .env
├── .gitignore
├── app.py
├── database.py
├── pyproject.toml
├── requirements.txt
├── test_database.py
├── uv.lock
└── README.md