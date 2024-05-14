import os
import streamlit as st
import numpy as np
from PIL import Image


st.set_page_config(page_title='my web app', page_icon=":tada", layout='wide')
if 'key' not in st.session_state:
    st.error('please login in your accont')
    st.stop()
if st.session_state['key'] is True:
    input_image = st.file_uploader("Upload Image 1", type=["jpg"])
    from deepface import DeepFace
    import cv2 as cv
    if input_image is not None:
        image = np.array(Image.open(input_image))
        image_6 = cv.resize(image, (500, 500))

    def processing(image):
        min_file = None
        x = None
        for file in os.listdir('new_database'):
            oop = file.split('.')[1]
            if oop == 'jpg':
                image_2 = f"new_database/{file}"
                mogayese = DeepFace.verify(image, image_2)
                if mogayese['verified']:
                    e = Image.open(f"new_database/{file}")
                    st.image([image, e], width=400)
                    x = True
                    break
                if min_file is None:
                    min_file = (file.split('.')[0], mogayese['distance'])
                else:
                    if min_file[1] > mogayese['distance']:
                        min_file = (file.split('.')[0], mogayese['distance'])
        if x is None:
            e = cv.imread(f"new_database/{min_file[0]}.jpg")
            e = cv.cvtColor(e, cv.COLOR_BGR2RGB)
            st.image([image, e])
                    
            
    w = st.button('start')
    if w and input_image is not None:
        try:
            processing(image_6)
        except:
            st.error('You have uploaded an inappropriate photo, please upload another photo')
