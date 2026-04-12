## Practice - 01

import streamlit as st # type: ignore

st.title(':red-background[Personal Info Card App]', anchor=False)
st.divider()

name = st.text_input('Enter Your Name', placeholder='Your Name Here')
age = st.number_input('Enter Your Age', placeholder='Your Age Here', value=None)
profession = st.selectbox('Enter Your Profession', ('Student', 'Employee', 'Businessman', 'Freelancer'), index=None)

button = st.button('Generate Card')

if button:
  if((name and age and profession)):
    st.write(f"Your name is {name}, you are {age} years old and your profession is {profession}.")
    st.success('Card Generated Successfully!')
  else:
    st.warning('Please fill all the fields')
    
    
