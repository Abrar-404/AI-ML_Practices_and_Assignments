import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from PIL import Image

# loading the environmental variables
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

# initializing a client
client = genai.Client(api_key=api_key)


# Image section
images = st.file_uploader(
  "Upload the notes (images) here",
  type=["jpg", "jpeg", "png"],
  accept_multiple_files=True
)


if images:
    pil_images = []
    
    for img in images:
      pil_img = Image.open(img)
      pil_images.append(pil_img)
    
    prompt= '"Generate a summary of the notes in 3-4 sentences. Highlight the key points and important information to markdown from the notes. The summary should be concise and capture the main ideas presented in the notes."'
    
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[pil_images, prompt]
    )
  
    st.markdown(response.text)