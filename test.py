import streamlit as st

st.header("Show your image")

uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    with st.container(horizontal_alignment="center"):
        st.image(uploaded_file,  use_container_width=True)