import streamlit as st
import pandas as pd
import requests
import json
from PIL import Image
import io


###
import warnings
from fastai.vision.all import *
from fastcore.parallel import *
import pickle
import numpy as np


warnings.filterwarnings('ignore')

learn = load_learner('.\model\CNN_Resnet.pkl', cpu=True)


###


st.write("""
# Convolutional Neural Network App
This app predicts wether you have pneumonia or not!
""")

st.markdown('Upload your image!!')

def load_image(image_file):
	img = Image.open(image_file)
	return img

st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

    
        data  = {'img':str(np.array(load_image(image_file)))}

        st.write(data)

        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                        "filesize":image_file.size}  
        st.write(file_details)

        # To View Uploaded Image
        st.image(load_image(image_file),width=450)


        if st.button("Predict"):
            url = "http://localhost:8000/api/v1/classify" # Aquí se pone la IP del contenedor de back "IP/api/v1/classify""
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, data=json.dumps(data))
            prediction = json.loads(response.text)#["Condition"]
            st.subheader('Prediction')
            st.write(prediction)

        # st.write(learn.predict(data['img'])[0])


