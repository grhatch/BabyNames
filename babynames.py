import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
df = pd.read_csv(
    'https://github.com/esnt/Data/raw/main/Names/popular_names.csv')

# Define the Streamlit app
st.title('Baby Name Popularity')

selected_name = st.text_input(
    "Type a name to search", placeholder="Enter a name of regular expression")

name_df = df[df['name'] == selected_name]

fig = px.line(name_df, x='year',
              y='n', color='sex', hover_data=['name'], color_discrete_map={'M': 'blue', 'F': 'pink'})
fig.update_layout(
    title=f'Popularity of the name, "{selected_name}" over time')
st.plotly_chart(fig)
