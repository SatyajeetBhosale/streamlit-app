import streamlit as st

st.title("My first app")
st.write("This app shows how to use streamlit to make it easy.")
st.text_input("Enter a name")
age=st.text_input("Enter your age")
if st.button("Submit"):
    if age.isdigit():
        st.success("Thank you for entering your age")
    else:
        st.error("Your age isn't a number")
