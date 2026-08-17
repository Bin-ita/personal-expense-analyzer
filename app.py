import streamlit as st
from database import initialize_database

st.set_page_config(
    page_title="Personal Expense Analyzer",
    page_icon="💰",
    layout="wide"
)

initialize_database()

st.title("💰 Personal Expense Analyzer & Budget Tracker")

st.write(
    "Track your income and expenses, manage your budget, "
    "and understand your spending habits."
)

st.success("Database connected successfully! 🎉")