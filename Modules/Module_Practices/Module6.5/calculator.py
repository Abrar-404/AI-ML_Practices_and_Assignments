import streamlit as st  # type: ignore

st.title('Goriber Calculator', anchor=False)
st.divider()

cols1, cols2, cols3 = st.columns(3)

with cols1:
  value1 = st.number_input('Enter first number', placeholder='Enter first number', value=None)
  
with cols2:
  operators = st.selectbox('Select an operator', ['+', '-', '*', '/'], index=None)
  
with cols3:
  value2 = st.number_input('Enter second number', placeholder='Enter second number', value=None)
  
button = st.button('Calculate', use_container_width='true')


if button:
  if (value1 is not None and operators is not None and value2 is not None):
    if(operators == "+"):
      result = value1 + value2
      st.markdown(f'{result}')
    elif(operators == "-"):
      result = value1 - value2
      st.markdown(f'{result}')
    elif(operators == "*"):
      result = value1 * value2
      st.markdown(f'{result}')
    elif(operators == "/"):
      try:
        result = value1 / value2
        st.markdown(f'{result}')
      except ZeroDivisionError:
        st.error('Cannot divide by zero')
  else:
    st.error('Please enter both numbers')
