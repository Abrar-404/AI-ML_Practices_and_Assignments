from gtts import gTTS
import streamlit as st
import io


text = "Hello, this is a test of the text to speech conversion using gTTS library in Python."

speech = gTTS(text, lang='en', slow=False)

speech.save('audio.mp3')

audio_buffer = io.BytesIO()

speech.write_to_fp(audio_buffer)

st.audio('audio.mp3')