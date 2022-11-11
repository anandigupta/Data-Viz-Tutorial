#import relevant libraries (first streamlit)
import streamlit as st
import pandas as pd
import plotly as py
import plotly.graph_objs as pg
import plotly.express as px


st.title("Data Visualization Tutorial: Interactive Streamlit Dashboard")
st.title("Anandi Gupta")


"""
This tutorial provides users a step-by-step guide for creating their own interactive data visualization dashboards using Streamlit and Plotly.

Note, to insert text blocks as shown here, simply type your text within a doc string.
"""

## URLs - Our world in data github as an example
#Emissions
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
#read in our world in data github
df_emissions = pd.read_csv(url)

df_emissions = df_emissions[['iso_code', 'country', 'year', 'co2', 'co2_per_capita', 'energy_per_gdp', 'energy_per_capita', 'population']]

#### Create relevant sections and corresponding plots using plotly

if st.sidebar.checkbox("Bar Charts Over Time", key="section1"):
    st.header("Example Bar Chart (Use st.header to include meaningful section header)")
    df_emissions_viz = df_emissions[df_emissions['country'] == "World"]
    df_emissions_viz = df_emissions_viz[df_emissions_viz['year'] > 1980].reset_index()
    fig = px.bar(df_emissions_viz, x=df_emissions_viz['year'], y=df_emissions_viz['co2'], labels={'co2':'Global CO2 Emissions', "year": "Year"},
                 title='CO2 Emissions Over Time')
    st.plotly_chart(fig, use_container_width=True)
    st.write("Use st.write to insert a meaningful takeaway")

if st.sidebar.checkbox("Chloropleth Maps", key="section2"):
    st.header("Example Chloropleth Map: Use st.header to include meaningful section header")

    answer1 = st.selectbox(label="Choose indicator",
    options=("CO2 Emissions Per Capita", "Energy Consumption Per Capita"))
    answer2 = st.slider('Choose time period', 2016, 2020, 2016)

    def cc_causes_maps(var):
        df_emissions2 = df_emissions[df_emissions['year'] == answer2]

        data = dict(type='choropleth',
                locations = df_emissions2['iso_code'],
                z = df_emissions2[var],
                text = df_emissions2['country'])

        layout = dict(title = answer1,
                  geo = dict(showframe = False,
                           projection = {'type':'robinson'},
                           showlakes = True,
                           lakecolor = 'rgb(0,191,255)'))
        x = pg.Figure(data = [data], layout = layout)
        st.plotly_chart(x, use_container_width=True)

    if answer1 == "CO2 Emissions Per Capita":
        cc_causes_maps('co2_per_capita')
        st.write("Use st.write to insert a meaningful takeaway about CO2 Emissions per Capita")

    elif answer1 == "Energy Consumption Per Capita":
        cc_causes_maps('energy_per_capita')
        st.write("Use st.write to insert a meaningful takeaway about Energy Consumption per Capita")

if st.sidebar.checkbox("Text Section", key="section6"):
    st.header("Use st.header to insert meaningful text header")
    """
    Insert any text within doc strings

    To add links use format "[NAME] (LINK)" as seen in the example below:

    1) [Anandi Gupta's Streamlit Dashboard](https://anandigupta-data-science-i-ds2-final-project-streamlit-2-fahu9f.streamlit.app/)
    """
