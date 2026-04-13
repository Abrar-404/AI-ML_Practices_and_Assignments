import streamlit as st # type: ignore

st.title(':red-background[Text Style Explorer]', anchor=False)
st.divider()

texts = st.text_input('Enter Your Texts', placeholder='Type something here...', value=None)

button = st.button('Display')

if button:
  if texts:
    functions = [st.title, st.header, st.subheader, st.text]
    
    for func in functions:
      st.divider()
      func(texts)