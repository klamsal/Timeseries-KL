import streamlit as st

# Set up the title and instructions with colorful text
st.markdown("<h1 style='color: teal;'>Fun Adding App for Toddlers</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: orange;'>Let's add two numbers together!</h3>", unsafe_allow_html=True)

# Ask for the first number
first_number = st.number_input("Enter the first number:", min_value=0, step=1, format="%d")

# Ask for the second number
second_number = st.number_input("Enter the second number:", min_value=0, step=1, format="%d")

# Calculate the sum when both numbers are entered
if st.button("Add Numbers"):
    result = first_number + second_number
    st.markdown(
        f"<h2 style='color: green;'>The sum is: {result}</h2>", 
        unsafe_allow_html=True
    )

# Adding a colorful footer
st.markdown("<p style='color: purple; font-size: 16px;'>Enjoy adding numbers, little mathematician!</p>", unsafe_allow_html=True)
