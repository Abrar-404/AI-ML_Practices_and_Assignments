import streamlit as st # type: ignore

st.title('Input your files', anchor=False)
st.divider()

# from folder
st.video('video/video.mp4', loop= True, start_time=0)

# upload
video = st.file_uploader('Upload your video file', type=['mp4', 'avi', 'mov', 'mkv'])

button = st.button('Click to upload video')

if button:
  if video:
    st.video(video)
    st.success('Video uploaded successfully!')
  else:
    st.error('Please upload a video file before clicking the button.')