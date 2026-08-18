from datetime import date

from flask import Flask, render_template, request, redirect, url_for

from database import (
    add_transaction,
    get_transactions,
    get_dashboard_summary,
    get_category_expenses,
    get_income_expense_totals,
    set_budget,
    get_budget,
    get_monthly_expenses,
    update_transaction,
    delete_transaction
)


app = Flask(__name__)


@app.route("/")
def home():

    summary = get_dashboard_summary()
    category_expenses = get_category_expenses()
    income_expense_totals = get_income_expense_totals()

    current_month = date.today().strftime("%Y-%m")

    budget = get_budget(current_month)
    monthly_expenses = get_monthly_expenses(current_month)

    remaining_budget = max(budget - monthly_expenses, 0)

    if budget > 0:
        budget_percentage = min(
            (monthly_expenses / budget) * 100,
            100
        )
    else:
        budget_percentage = 0

    return render_template(
        "dashboard.html",
        summary=summary,
        category_expenses=category_expenses,
        income_expense_totals=income_expense_totals,
        budget=budget,
        monthly_expenses=monthly_expenses,
        remaining_budget=remaining_budget,
        budget_percentage=budget_percentage,
        current_month=current_month
    )


@app.route("/add", methods=["GET", "POST"])
def add_transaction_page():

    if request.method == "POST":

        transaction_type = request.form["transaction_type"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        transaction_date = request.form["date"]
        description = request.form["description"]

        add_transaction(
            transaction_date,
            transaction_type,
            category,
            description,
            amount
        )

        return redirect(url_for("transactions_page"))

    return render_template("add_transaction.html")


@app.route("/transactions")
def transactions_page():

    transactions = get_transactions()

    categories = sorted(
        set(transaction.category for transaction in transactions)
    )

    selected_category = request.args.get("category", "")

    if selected_category:
        transactions = [
            transaction
            for transaction in transactions
            if transaction.category == selected_category
        ]

    return render_template(
        "transactions.html",
        transactions=transactions,
        categories=categories,
        selected_category=selected_category
    )


@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction_page(transaction_id):

    transactions = get_transactions()

    transaction = next(
        (
            item
            for item in transactions
            if item.id == transaction_id
        ),
        None
    )

    if transaction is None:
        return "Transaction not found", 404

    if request.method == "POST":

        transaction_type = request.form["transaction_type"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        transaction_date = request.form["date"]
        description = request.form["description"]

        update_transaction(
            transaction_id,
            transaction_date,
            transaction_type,
            category,
            description,
            amount
        )

        return redirect(url_for("transactions_page"))

    return render_template(
        "edit_transaction.html",
        transaction=transaction
    )


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction_page(transaction_id):

    delete_transaction(transaction_id)

    return redirect(url_for("transactions_page"))


@app.route("/budget", methods=["GET", "POST"])
def budget_page():

    current_month = date.today().strftime("%Y-%m")

    if request.method == "POST":

        month = request.form["month"]
        amount = float(request.form["amount"])

        set_budget(month, amount)

        return redirect(url_for("budget_page"))

    budget = get_budget(current_month)
    monthly_expenses = get_monthly_expenses(current_month)

    remaining_budget = max(budget - monthly_expenses, 0)

    if budget > 0:
        budget_percentage = min(
            (monthly_expenses / budget) * 100,
            100
        )
    else:
        budget_percentage = 0

    return render_template(
        "budget.html",
        budget=budget,
        monthly_expenses=monthly_expenses,
        remaining_budget=remaining_budget,
        budget_percentage=budget_percentage,
        current_month=current_month
    )


if __name__ == "__main__":
    app.run(debug=True)