import streamlit as st
import pandas as pd

st.title("📊VIEW EXPENSES")
file = "expenses.csv"
df = pd.read_csv(file)
st.dataframe(df)
st.write(f"Total Expenses: {df['amount'].sum()} ₨")
if st.button:
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="expenses.csv",
        mime="text/csv"
    )



