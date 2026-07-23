import streamlit as st

st.title("Pyhton Basics Parogramming")


with st.expander("Q-1 -Personal Information"):
    name = st.text_input("Enter your name:")
    city = st.text_input("Enter your city:")

if st.button("Submit"):
    st.success(f"Name: {name}")
    st.success(f"City: {city}")

with st.expander("Q-2 - Arithmetic Operations"):
    num1 = st.number_input("Enter first number:", value=None)
    num2 = st.number_input("Enter second number:", value = None)

    operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        num1 = int(num1)
        num2 = int(num2)
        if operation == "Addition":
            result:  int = num1 + num2
        elif operation == "Subtraction":
            result:  int = num1 - num2
        elif operation == "Multiplication":
            result:  int = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result:  float = num1 / num2
            else:
                result = "Error: Division by zero"
        st.success(f"Result: {result}")