import streamlit as st # type: ignore

st.title(':red-background[Image Gallery App]', anchor=False)
st.divider()

images = st.file_uploader("Upload Your Images Here", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

button = st.button('Upload Images')

if button:
  if images:
    if(len(images) > 3):
      st.error('You can only upload a maximum of 3 images.')
    else:
        cols = st.columns(len(images))
        st.success('Images Uploaded Successfully!')

        for i, img in enumerate(images):
          with cols[i]:
            st.image(img, caption=img.name)
            
        
        if len(images) == 3:
          st.success('Exactly 3 images uploaded successfully!')
        else:
          remaining = 3 - len(images)
          st.info(f'You have uploaded {len(images)} image(s). You can upload up to 3 total. {remaining} more image(s) can be uploaded.')
            
        
  else:
    st.error('Please upload at least one image.')