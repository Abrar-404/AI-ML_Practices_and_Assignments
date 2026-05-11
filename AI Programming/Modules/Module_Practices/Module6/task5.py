import streamlit as st # type: ignore
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title(':red-background[Gemini Chatbot App]', anchor=False)
st.divider()

qus = st.text_input('Enter your query here:', placeholder='Enter your query here...')

button = st.button('Ask Gemini')

if button:
  if qus:
    response = client.models.generate_content(
      model = 'gemini-flash-lite-latest',
      contents={qus}
    )
    st.markdown(f':green-background[{response.text}]')
    
  else:
    st.error('Please enter a query before asking Gemini.')