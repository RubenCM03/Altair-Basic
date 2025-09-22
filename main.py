import streamlit as st


movies = st.Page("movies.py", title="Movies", icon=":material/add_circle:")
cars = st.Page("cars.py", title="Cars", icon=":material/add_circle:")
test = st.Page("test.py", title="Test", icon=":material/add_circle:")

pg = st.navigation([movies,cars,test])
st.set_page_config(
    page_title="RCM Altair",
    page_icon="𝚾",
    initial_sidebar_state="expanded"
)

pg.run()