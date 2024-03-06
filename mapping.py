import folium
from folium.plugins import MarkerCluster
import pandas as pd

from plotting import CityNotFoundException


def create_map(data_frames, location, output_filename):
    # Locate the correct DataFrame based on the specified location
    if location == 'Albany':
        data = data_frames[0]
    elif location == 'Athens':
        data = data_frames[1]
    elif location == 'Amsterdam':
        data = data_frames[2]
    elif location == 'Antwerp':
        data = data_frames[3]
    elif location == 'Bangkok':
        data = data_frames[4]
    else:
        raise CityNotFoundException(f"{location} not found")

    # Initialize the map centered around the mean latitude and longitude of the data
    m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], tiles='CartoDB positron', zoom_start=10)

    # Initialize MarkerCluster
    marker_cluster = MarkerCluster().add_to(m)

    # Add points to the MarkerCluster
    for idx, row in data.iterrows():
        if pd.notna(row['latitude']) and pd.notna(row['longitude']):
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"Price: {row['price']}<br>Reviews: {row['number_of_reviews']}<br>Min Nights: {row['minimum_nights']}", max_width=300),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)

    # Save the map to an HTML file
    m.save(output_filename)