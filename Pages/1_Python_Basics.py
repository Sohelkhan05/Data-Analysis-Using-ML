from os import write

from itsdangerous import NoneAlgorithm
import streamlit as st
import pandas as pd

st.title("Pyhton Basics Parogramming")
st.header("Part - A : Python Basics Programming")


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

with st.expander("Q-3 - String Functions"):
    input_string = st.text_input("Enter a string:")

    if st.button("Process String"):
        length = len(input_string)
        uppercase = input_string.upper()
        lowercase = input_string.lower()

        st.success(f"Length: {length}")
        st.success(f"Uppercase: {uppercase}")
        st.success(f"Lowercase: {lowercase}")

with st.expander("Q-4 - String Formating"):
    name = st.text_input("Enter your student name:")
    age = st.number_input("Enter your student age:", value=0)

    if st.button("Format String"):
        formatted_string = f"My name is {name} and I am {age} years old."
        st.success(formatted_string)

st.header("Part - B : Wrking with Listes and Dictionaries")

with st.expander("Q-5 - Nested List Access "):
    lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    st.success(lst[3][1][2][0]) 

with st.expander("Q-6 - Nested Dictionary Access"):
    d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
    st.success(d['k1'][3]['tricky'][3]['target'][3])

with st.expander("Q-7 - Difference between List and Tuple"):
    data = {
    "List": [
        "Lists are mutable, meaning their elements can be changed after creation.",
        "Lists are defined using square brackets [].",
        "Lists consume more memory due to their dynamic nature.",
        "Lists have more built-in methods for manipulation."
    ],
    "Tuple": [
        "Tuples are immutable, meaning their elements cannot be changed after creation.",
        "Tuples are defined using parentheses ().",
        "Tuples consume less memory and are generally faster than lists.",
        "Tuples have fewer built-in methods compared to lists."
    ]
    }

    df = pd.DataFrame(data)
    st.table(df)

st.header("part - C : User Defined Functions")

with st.expander("Q-8 - Email Domain Extraction"):
    email = st.text_input("Enter your email address:")

    if st.button("Extract Domain"):
        if "@" in email:
            domain = email.split("@")[1]
            st.success(f"Domain: {domain}")
        else:
            st.error("Invalid email address. Please enter a valid email.")

with st.expander("Q-9 - Dog Finder"):
    def find_dog(s):
        return 'dog' in s.lower().split()

    st.success(find_dog('Is dog'))

with st.expander("Q-10 - Dog Counter"):
    def count_dog(s):
        return s.lower().split().count('dog')

    st.success(count_dog('This dog  dog dog dog runs faster than the other dog dude!'))

st.header("Part - D : Conditional Statements")
with st.expander("Q-11 - Speeding Ticket Calculator"):
    def caught_speeding(speed, is_birthday):
        if is_birthday:
            speed -= 5  # Allow 5 extra mph on birthday

        if speed <= 60:
            return "No Ticket"
        elif 61 <= speed <= 80:
            return "Small Ticket"
        else:
            return "Big Ticket"

    st.success(caught_speeding(81, True))
    st.success(caught_speeding(81, False))

st.header("Part - E : Additional Exercises")
with st.expander("Q-12 - Menu-Driven Application"):
    st.write("1. Extract Email Domain")
    st.write("2. Find word dog in sentence")
    st.write("3. Count word dog in sentence")
    st.write("4. Exit")


    choice = st.number_input("Enter your choice (1-4):", value=None, step=1)
    if choice == 1:
        email = st.text_input("Enter email address:")
        domain = email.split("@")[-1]
        st.success(f"Domain: {domain}")
    elif choice == 2:
        sentence = st.text_input("Enter a sentence:")
        st.success("dog" in sentence.lower())
    elif choice == 3:
        sentence = st.text_input("Enter a sentence:")
        st.success(sentence.lower().split().count('dog'))
    elif choice == 4:
        st.success("Exiting...")
    else:
        st.write("Invalid Choice.")

with st.expander("Q-13 - Student Calculator"):
    sub1 = st.number_input("Enter marks for subject 1:", value=0)
    sub2 = st.number_input("Enter marks for subject 2:", value=0)
    sub3 = st.number_input("Enter marks for subject 3:", value=0)  
    sub4 = st.number_input("Enter marks for subject 4:", value=0)  
    sub5 = st.number_input("Enter marks for subject 5:", value=0)

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    else:
        grade = 'F'
    if st.button("Calculate Result"):
        st.success("----- Result -----")
        st.success(f"Total: {total}")
        st.success(f"Percentage: {percentage}%")
        st.success(f"Grade: {grade}")
