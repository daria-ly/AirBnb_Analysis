## AirBnb Data Analysis
A Python Data Science project focused on analyzing a dataset of AirBnb rentals in different locations and outputting it in a user-friendly GUI.

## Features
-** Interactive Maps: Displaying Airbnb listings with details on hover.
-** Data Visualization: Visualizations of room types and license statuses of listings.
-** Navigable Cities: Users can switch between cities to view respective data.
-** Dynamic Visualizations: Charts and maps are loaded based on the selected city.

## Installation
Ensure Python 3.6+ is installed. Clone this repository, then install dependencies:

## Running the Application
Execute the application with:

Place the Airbnb listings data in the specified directory. 
The expected format for each city's CSV includes columns like id, name, latitude, longitude, room_type, price, etc.

## Project Structure
-** Main.py: Initializes and runs the GUI application.
-** Gui.py: Contains the DataVisualizationApp class for the main window.
-** Plotting.py: Functions for generating statistical charts.
-** Mapping.py: Generates interactive maps using folium.

## Data Requirements
Data files should be CSV format, with columns for listing details such as id, name, host_id, latitude, longitude, room_type, and others.
