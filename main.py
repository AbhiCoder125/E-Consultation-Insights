import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')
st.button('Hi I am Abhinag')
name =st.text_input('Enter your name')
age = st.text_input('Enter your age')
goal = st.text_input('Enter your goal')

st.write(f'Hello {name}! You are {age} years old and your goal is {goal}.')
