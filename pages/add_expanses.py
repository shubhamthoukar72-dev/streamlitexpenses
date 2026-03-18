import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("➕ADD EXPENSES")
file = "expenses.csv"

if os.path.exists(file):
    df = pd.read_csv(file)
    df.to_csv(file, index=False)
expense_date = st.date_input("Date", date.today())
category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])
amount = st.number_input("Amount", min_value=0.0)
note= st.text_input("Note")
if st.button("Add Expense"):
    df =pd.read_csv(file) 

    new_data = pd.DataFrame({
        "date": [expense_date],
        "category": [category],
        "amount": [amount],
        "note": [note]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file, index=False)
    
    st.success("Expense added successfully!")