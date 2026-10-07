#1. Install  Streamlit in terminal of vs code(pip install stramlit)

import streamlit as st

st.title("My First web app!")

name=st.text_input("What is your name?")
age=st.number_input("What is your age?")

if st.button("Say hello!"):
    st.write(f"Hello{name}, you are{age} years old!")

    #Launch the web app(streamlit run webapp.py)