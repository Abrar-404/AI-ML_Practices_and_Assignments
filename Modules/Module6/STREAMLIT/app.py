from google import genai
import os
from dotenv import load_dotenv
import streamlit as st # type: ignore

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
  model='gemini-3.1-flash-lite-preview',
  contents='Give me an idea of AI/ML in 50 words'
)

st.markdown(response.text)