
import streamlit as st # type: ignore

st.title(':red-background[Audio & Video Player App]', anchor=False)
st.divider()

audio = st.file_uploader('Upload an audio file', type=['mp3', 'ogg'])
video = st.file_uploader('Upload a video file', type=['mp4', 'mkv'])

play_button = st.button('Play Audio/Video')


if play_button:
  if not audio and not video:
    st.error('No file uploaded! Please upload an audio or video file first.')
  else:
    if audio:
      st.subheader('🎵 Audio Player')
      st.audio(audio)
      
    if video:
      st.subheader('🎬 Video Player')
      st.video(video)
      
    st.success('Audio/Video played successfully!')