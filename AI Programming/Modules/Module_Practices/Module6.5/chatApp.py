import streamlit as st  # type: ignore
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

st.title('Chat App', anchor=False)
st.divider()

content = st.text_input("Enter your prompt", placeholder="What's on your mind?")
button = st.button('Generate :streamlit:', use_container_width=True)

if button:
  if content:
    response = client.models.generate_content(
      model="gemini-flash-lite-latest",
      contents=content
    )
    st.markdown(f"{response.text}")
  else:
    st.error("Please enter a prompt to generate content.")