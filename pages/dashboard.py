import streamlit as st
import pandas as pd

st.title("📊 EXPENSES DASHBOARD")

file = "expenses.csv"

def load_expenses(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["date", "category", "amount", "note"])
        df.to_csv(path, index=False)
        return df

df = load_expenses(file)

if df.empty:
    st.info("No expenses recorded yet. Please add some expenses to see the dashboard.")
else:
    st.write("### Total Expenses by Category")
    category_summary = df.groupby("category")["amount"].sum()
    st.bar_chart(category_summary)

    st.write("### Category Summary")
    st.write(category_summary)

    st.write("### Daily Expenses Over Time")
    df["date"] = pd.to_datetime(df["date"])
    daily_summary = df.groupby("date")["amount"].sum()
    st.line_chart(daily_summary)