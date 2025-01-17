import streamlit as st
import plotly.express as px

# List of countries categorized as Democratic or Autocratic
countries = [
    "Switzerland", "USA", "Germany", "India", "Brazil", "Australia", "France", 
    "Russia", "China", "Saudi Arabia", "North Korea", "Turkey", "Iran", "Cuba"
]

# Manually defining regime type for each country (Democratic = 1, Autocratic = 0)
regimes = {
    "Switzerland": "Democratic",
    "USA": "Democratic",
    "Germany": "Democratic",
    "India": "Democratic",
    "Brazil": "Democratic",
    "Australia": "Democratic",
    "France": "Democratic",
    "Russia": "Autocratic",
    "China": "Autocratic",
    "Saudi Arabia": "Autocratic",
    "North Korea": "Autocratic",
    "Turkey": "Autocratic",
    "Iran": "Autocratic",
    "Cuba": "Autocratic"
}

# Create a color mapping for regime types
color_map = {
    "Democratic": "blue",  # Blue for Democratic countries
    "Autocratic": "red"    # Red for Autocratic countries
}

# Create a list of colors corresponding to each country
colors = [color_map[regimes[country]] for country in countries]

# Create the map using Plotly Express
fig = px.choropleth(locations=countries, 
                    color=[regimes[country] for country in countries], 
                    locationmode='country names', 
                    title='Democratic vs Autocratic Countries',
                    color_continuous_scale=['blue', 'red'],  # Blue for Democratic, Red for Autocratic
                    labels={'color': 'Regime Type'})

# Update map appearance
fig.update_geos(showcoastlines=True, coastlinecolor="Black", projection_type="mercator")
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True, projection_scale=2),
    coloraxis_colorbar=dict(title="Regime Type")
)

# Streamlit app
st.title('Map of Democratic and Autocratic Countries')
st.plotly_chart(fig)
