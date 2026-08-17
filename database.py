import sqlite3

DATABASE_NAME = "expense_tracker.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """Create the transactions table if it does not already exist."""
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()