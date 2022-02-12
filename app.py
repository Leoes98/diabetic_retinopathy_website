import streamlit as st
import requests

st.set_page_config(
    page_title=
    "AI DR Assistant",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="auto")


'''
# AI Diabetic Retinopathy Assistant
'''

st.write("""\
        This platform is meant to reduce the gap between AI and medicine. This AI DR assistant \
        is an accessible online system to support medical professionals during the diagnosis. \
            The physician uploads a retina image to be classified by the AI model.

        The prediction will show one of these outputs:
        * 0: No DR.
        * 1: Mild DR.
        * 2: Severe DR.
        """)


'''
#
'''
# Load Image
image = st.file_uploader("Choose a retina image to analyze..."
                         , type=["jpeg", 'jpg', 'png'])

if st.button("Make Prediction"):
    if image is not None:
        params = {"img_file": image.getvalue()}
        api_url = "https://gcp-api-dr-cwcjlajpfq-uc.a.run.app/predict"
        res = requests.post(api_url, files=params)
        pred = res.json()
        st.image(image, width=500)
        st.subheader("Prediction")
        if pred[-1][0] == 0:
            st.write(f"""
                     0: No DR.  \n It's likely that you don't have diabetic retinopathy.""")
        elif pred[-1][0] == 2:
            st.write(f"""
                     1: Mild DR.  \n You may have mild or moderate diabetic retinopathy, \
                we suggest a visit to an ophthalmologist for a screening.""")
        else:
            st.write("""
                     2: Severe DR.  \n You may have severe or proliferative diabetic retinopathy\
                , you should have a recurrent screening with your ophthalmologist.""")

st.subheader("Disclaimer")
st.write("This analysis does not replace an ophthalmologist diagnosis, \
    you should book an appointment with your doctor for further exams and treatment.")


st.subheader("About this app")
st.markdown("""
The data used to train the model can be found on Kaggle at: \
    https://www.kaggle.com/amanneo/diabetic-retinopathy-resized-arranged""")
st.markdown("""
            The authors of this project are:
            * [Leonardo Torres](https://github.com/Leoes98)
            * [Martin Morcos](https://github.com/bernamr)
            * [Nicolás Núñez](https://github.com/nico-nv)
""")
"""
Github source code:
* [Backend](https://github.com/Leoes98/diabetic_retinopathy_DL)
* [Frontend](https://github.com/Leoes98/diabetic_retinopathy_website)"""
