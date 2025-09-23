import streamlit as st

st.header("Show your image")

uploaded_file = st.file_uploader("Upload an image")
st.divider()
if uploaded_file is not None:
    if uploaded_file.name.endswith(".jpg") or uploaded_file.name.endswith(".png") or uploaded_file.name.endswith(".jpeg") or uploaded_file.name.endswith(".webp"):
        with st.container(horizontal_alignment="center"):
            st.image(uploaded_file,  use_container_width=True)
    else:
        with st.container(horizontal_alignment="center"):
            col1, col2 = st.columns(2)
            with col1:
                st.text('This is not an image file (JPG, JPEG, PNG, WEBP)!!!')
            with col2:
                st.badge("ERROR", color="red")
