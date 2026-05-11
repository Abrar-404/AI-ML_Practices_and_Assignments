import streamlit as st # type: ignore

st.title('Input your files', anchor=False)
st.divider()

# from folder
st.audio('audio/audio.mp3', loop= True, start_time=0)

# upload
audio = st.file_uploader('Upload your audio file', type=['mp3', 'wav', 'ogg', 'flac'])

if audio:
  st.audio(audio)