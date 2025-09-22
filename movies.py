from turtledemo import colormixer
import streamlit as st
import altair as alt
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.movies()

movies = load_data()

st.header("Movies")

if st.checkbox("Show raw data"):
    st.write(movies)
else:
    st.write(vega_datasets.data.movies.url)

chart = alt.Chart(movies).mark_bar().encode(
    alt.X('year(Release_Date):O', axis=alt.Axis(title='Year of Release')),
    alt.Y('count():Q', axis=alt.Axis(title='Number of Movies')),
    tooltip=[alt.Tooltip('year(Release_Date):O', title='Year'), alt.Tooltip('count():Q', title='Number of Movies')],
    color=alt.Color('count():Q').scale(scheme="reds")
)

st.write(chart)

chart = alt.Chart(movies).transform_filter(
    "(datum.Director != null)"
).mark_bar().encode(
    alt.Y('Director:N'),
    alt.X('count(Director):Q'),
    color=alt.Color('count(Director):Q').scale(scheme="greens")
)

st.write(chart)