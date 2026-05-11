import streamlit as st  # type: ignore
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

st.title('Paraphraser', anchor=False)
st.divider()

content = st.text_input("Enter your prompt", placeholder="What's on your mind?")
button = st.button('Generate :streamlit:', use_container_width=True)

if button:
  if content:
    try:
      response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=content,
        config=types.GenerateContentConfig(
        system_instruction="Paraphrase the following content in a more concise and clear manner. Do not add extra texts. Only paraphrase the content provided and Improve the provided sentence professionally.",
      ),
    )
      st.markdown(f"{response.text}")
    except Exception as e:
      st.error(f"Something went wrong: {e}")
  else:
    st.error("Please enter a prompt to generate content.")