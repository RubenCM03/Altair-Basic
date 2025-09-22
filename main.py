import polars as pl
import streamlit as st
import altair as alt
import vega_datasets


df = pl.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})
chart = alt.Chart(df).mark_point(color='firebrick').encode(
    alt.X('precip', scale=alt.Scale(type='log'), axis=alt.Axis(title='Log-Scaled Values')),
    alt.Y('city', axis=alt.Axis(title='Category')),
)

st.altair_chart(chart)

@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()

st.write(cars)

mpg = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)', axis=alt.Axis(title='Average Miles Per Gallon')),
)

hp = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Horsepower)',axis=alt.Axis(title='Average Horsepower')),
)

chart = mpg | hp

st.altair_chart(chart)

chart = alt.Chart(cars).mark_line(point=True).encode(
    alt.Y('Weight_in_lbs'),
    alt.X('Miles_per_Gallon', axis=alt.Axis(title='Average Miles Per Gallon')),
)

st.altair_chart(chart)

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin'] # show Name and Origin in a tooltip
).interactive()
st.altair_chart(chart)


