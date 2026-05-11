import streamlit as st # type: ignore

st.title('Input your files', anchor=False)
st.divider()

# internal folder image
# st.image('image/image.jpg') 

# url
st.image('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzloa3FrbWljc3RrN3RnaTQwczVmaHFkOHJnbW0zdmhnbnk2NTdvNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/78XCFBGOlS6keY1Bil/giphy.gif') 


st.divider()

image = st.file_uploader('Upload your Image (At max - 2)', type=['jpg', 'jpeg', 'png', 'pdf', 'gif'], accept_multiple_files=True, help='You can upload multiple files at once')

print(type(image))


if image:
  if(len(image) > 2):
    st.warning('Please upload a maximum of 2 images.')
    col = st.columns(len(image))
  
    for i, img in enumerate(image):
      with col[i]:
        st.image(img)
  