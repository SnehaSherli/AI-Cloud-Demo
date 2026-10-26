import streamlit as st

st.title("AI on Cloud Computing")
st.header("Welcome to My Cloud Application")

st.write(
    "This sample application demonstrates "
    "how to deploy a web application on the cloud."
)

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name.strip():
        st.success(f"Hello, {name}! Welcome to the cloud.")
    else:
        st.warning("Please enter your name.")