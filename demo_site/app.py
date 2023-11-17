import streamlit as st
import pandas as pd

st.set_page_config(page_title="Demo Page", page_icon=":tada:")


st.write("Here's our first attempt at using data to create a table: nopes")

# st.line_chart(chart_data)

map_data = pd.DataFrame(
   {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
})

st.map(map_data)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin","Dragon Ball")
    )
    st.write("---")
    st.write(f"You are in {chosen} house!")
    st.write("---")
