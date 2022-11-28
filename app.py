import streamlit as st

st.write("""Addition of Two numbers""")
st.header("Enter 2 Numbers For Addition")

First_Number = st.number_input("Enter 1st Number")
Second_Number = st.number_input("Enter 2nd Number")
st.write('Sum of Two Numbers', First_Number+Second_Number)