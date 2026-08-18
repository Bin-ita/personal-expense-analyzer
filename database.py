import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Float, select, func
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Mapped,
    mapped_column
)


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set in the .env file"
    )


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


class Transaction(Base):

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    date: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    transaction_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255)
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )


class Budget(Base):

    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    month: Mapped[str] = mapped_column(
        String(7),
        unique=True,
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )


Base.metadata.create_all(engine)


# ==========================================
# ADD TRANSACTION
# ==========================================

def add_transaction(
    date,
    transaction_type,
    category,
    description,
    amount
):

    session = SessionLocal()

    try:

        transaction = Transaction(
            date=date,
            transaction_type=transaction_type,
            category=category,
            description=description,
            amount=amount
        )

        session.add(transaction)

        session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


# ==========================================
# GET TRANSACTIONS
# ==========================================

def get_transactions():

    session = SessionLocal()

    try:

        statement = (
            select(Transaction)
            .order_by(Transaction.date.desc())
        )

        return session.scalars(statement).all()

    finally:

        session.close()


# ==========================================
# DASHBOARD SUMMARY
# ==========================================

def get_dashboard_summary():

    session = SessionLocal()

    try:

        income = session.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )
            )
            .where(
                Transaction.transaction_type == "Income"
            )
        )

        expenses = session.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )
            )
            .where(
                Transaction.transaction_type == "Expense"
            )
        )

        transaction_count = session.scalar(
            select(func.count(Transaction.id))
        )

        balance = income - expenses

        return {

            "income": float(income),

            "expenses": float(expenses),

            "balance": float(balance),

            "transaction_count": transaction_count

        }

    finally:

        session.close()


# ==========================================
# CATEGORY EXPENSES
# ==========================================

def get_category_expenses():

    session = SessionLocal()

    try:

        results = session.execute(

            select(
                Transaction.category,
                func.sum(Transaction.amount)
            )

            .where(
                Transaction.transaction_type == "Expense"
            )

            .group_by(
                Transaction.category
            )

            .order_by(
                func.sum(Transaction.amount).desc()
            )

        ).all()


        return [

            {
                "category": category,
                "amount": float(amount)
            }

            for category, amount in results

        ]

    finally:

        session.close()


# ==========================================
# INCOME VS EXPENSE TOTALS
# ==========================================

def get_income_expense_totals():

    session = SessionLocal()

    try:

        results = session.execute(

            select(
                Transaction.transaction_type,
                func.sum(Transaction.amount)
            )

            .group_by(
                Transaction.transaction_type
            )

        ).all()


        return [

            {
                "type": transaction_type,
                "amount": float(amount)
            }

            for transaction_type, amount in results

        ]

    finally:

        session.close()


# ==========================================
# SET BUDGET
# ==========================================

def set_budget(month, amount):

    session = SessionLocal()

    try:

        budget = session.scalar(

            select(Budget)
            .where(Budget.month == month)

        )


        if budget:

            budget.amount = amount

        else:

            budget = Budget(

                month=month,

                amount=amount

            )

            session.add(budget)


        session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


# ==========================================
# GET BUDGET
# ==========================================

def get_budget(month):

    session = SessionLocal()

    try:

        budget = session.scalar(

            select(Budget)
            .where(Budget.month == month)

        )


        if budget:

            return float(budget.amount)

        return 0.0

    finally:

        session.close()


# ==========================================
# MONTHLY EXPENSES
# ==========================================

def get_monthly_expenses(month):

    session = SessionLocal()

    try:

        expenses = session.scalar(

            select(

                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )

            )

            .where(

                Transaction.transaction_type == "Expense",

                Transaction.date.like(
                    f"{month}%"
                )

            )

        )


        return float(expenses)

    finally:

        session.close()


# ==========================================
# UPDATE TRANSACTION
# ==========================================

def update_transaction(
    transaction_id,
    date,
    transaction_type,
    category,
    description,
    amount
):

    session = SessionLocal()

    try:

        transaction = session.get(
            Transaction,
            transaction_id
        )


        if transaction:

            transaction.date = date

            transaction.transaction_type = (
                transaction_type
            )

            transaction.category = category

            transaction.description = (
                description
            )

            transaction.amount = amount

            session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


# ==========================================
# DELETE TRANSACTION
# ==========================================

def delete_transaction(transaction_id):

    session = SessionLocal()

    try:

        transaction = session.get(
            Transaction,
            transaction_id
        )


        if transaction:

            session.delete(transaction)

            session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()