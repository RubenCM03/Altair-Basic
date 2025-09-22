import streamlit as st
import altair as alt
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()

st.header("Cars")

if st.checkbox("Show raw data"):
    st.write(cars)
else:
    st.write(vega_datasets.data.cars.url)

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


