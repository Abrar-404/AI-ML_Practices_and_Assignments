import streamlit as st  # type: ignore

st.title("Draft Task")
st.divider()


#============ task 1 ================

# name = st.text_input('Enter your name', placeholder="Enter your name here")
# age = st.number_input('Enter your age', placeholder='Enter your age here', value = None)
# profession = st.selectbox('Enter your profession', ('Student', 'Employee', 'Businessman', 'Freelancer'), index=None)

# button = st.button('Submit')

# if button:
#   if(name and age and profession):
#     st.success('Card Generated Successfully!')
#     st.write(f"Hello {name}, you are {age} years old and your profession is {profession}.")
#   else:
#     st.warning('Please fill all the fields')


#============ task 2 ================

# This code snippet is a Streamlit application that allows users to upload images and displays them on
# the interface. Here's a breakdown of what the code does:
# images = st.file_uploader('Upload your file', type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)
# button = st.button('Upload')

# if button:
#   if images:
#     if(len(images) > 3):
#       st.error('You can only upload a maximum of 3 images.')
#     else:
#       cols = st.columns(len(images))
      
#       for i, img in enumerate(images):
#         with cols[i]:
#           st.image(img)
  
      
#       if (len(images) == 3):
#         st.success('Images uploaded successfully!')
#       elif(len(images) < 3):
#         remaining = 3 - len(images)
#         st.info(f'You have uploaded {len(images)} image(s). You can upload up to 3 total. {remaining} more image(s) can be uploaded.')
    
#   if not images:
#     st.error('Please upload at least one image.')


#============ task 3 ================

# audio = st.file_uploader('Upload your audio file', type=['mp3', 'ogg'])
# video = st.file_uploader('Upload your video file', type=['mp4', 'mkv'])

# button = st.button('Play')

# if button:
#   if audio or video:
#     if audio:
#       st.audio(audio)
#     if video:
#       st.video(video)
#   else:
#     st.error('Please Upload a file first.')



#============ task 4 ================

# text_display = st.text_input('Enter some text to display', placeholder='Enter your text here')

# button = st.button('Display')

# if button:
#   if text_display:
#     functions = [st.title, st.header, st.subheader, st.text]
    
#     for func in functions:
#       st.divider()
#       func(text_display)
