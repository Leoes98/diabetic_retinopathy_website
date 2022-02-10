import streamlit as st
import requests

st.set_page_config(
    page_title=
    "DR prediction interface",  # => Quick reference - Streamlit
    page_icon="⚕️",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed


'''
# Diabetic Retinopathy Interface
'''

'''
#
'''
# Load Image
image = st.file_uploader("Choose an image", type=["jpeg", 'jpg', 'png'])

if st.button("Make Prediction"):
    if image is not None:
        params = {"img_file": image.getvalue()}
        api_url = "https://gcp-api-dr-cwcjlajpfq-uc.a.run.app/predict"
        res = requests.post(api_url, files=params)
        pred = res.json()
        st.image(image, width=500)
        st.write(f"Class: {pred[-1][0]}")
        st.write(f"Probability: {pred[-1][1]/100}%")
