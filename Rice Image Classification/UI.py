import streamlit as st
import requests

API_URL = "https://unsubversive-monica-semistiff.ngrok-free.dev/predict"

st.title("Rice Classification")

uploaded_file = st.file_uploader(
    "Upload Rice Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file)

    if st.button("Predict"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(response.text)