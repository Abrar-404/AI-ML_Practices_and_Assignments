import streamlit as st # type: ignore

st.title(':point_right: Initializing Web App in Python', anchor=False)
st.header('Content 1', divider=True)
st.subheader('Content 1 subheader')
st.text('Text goes here :point_left:')
st.markdown('**:red[Text goes]** *here* :point_left:')
st.markdown(':red-background[**:orange[Text goes]** *here*]:point_left:')

a = 10
b = 20
st.write(a, b)