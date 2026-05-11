import streamlit as st # type: ignore

st.title('Input your information', anchor=False)
st.divider()

name = st.text_input('Enter your name', placeholder='Type your name here')

age = st.number_input('Enter your age', value=None, placeholder='Type your age here')

pressed = st.button('Enter to submit', type='secondary')

selectbox = st.selectbox('Choose or add your profession', ('Developer', 'Designer', 'Manager'), placeholder='Select or add your profession', index = None, accept_new_options = True)
st.write('Your profession is:', selectbox)

if pressed:
  st.write(f"Your name is {name} and your age is {age}")

# password = st.text_input('Enter your password', placeholder='Type your password here', type='password')
# st.write('Your name is:', password)
# st.divider()