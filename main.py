# main.py
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QUrl
import os
import sys

from gui import DataVisualizationApp
from plotting import plot_room_type_distribution, plot_license_distribution
from mapping import create_map

def load_data():
    files = [
        '/Users/lyk-dar/Desktop/AlbanyUSA.csv',
        '/Users/lyk-dar/Desktop/AthensGreece.csv',
        '/Users/lyk-dar/Desktop/Amsterdam.csv',
        '/Users/lyk-dar/Desktop/AntwerpBelgium.csv',
        '/Users/lyk-dar/Desktop/BangkokThailand.csv'
    ]
    data_frames = [pd.read_csv(file) for file in files]
    return data_frames

def calculate():

    data_frames = load_data()

    # Calculate raw counts of each room type for each location.
    room_type_counts_Albany = data_frames[0]['room_type'].value_counts()
    room_type_counts_Athens = data_frames[1]['room_type'].value_counts()
    room_type_counts_Amsterdam = data_frames[2]['room_type'].value_counts()
    room_type_counts_Antwerp = data_frames[3]['room_type'].value_counts()
    room_type_counts_Bangkok = data_frames[4]['room_type'].value_counts()

    #total number of data points
    total_Albany = len(data_frames[0])
    total_Athens = len(data_frames[1])
    total_Amsterdam = len(data_frames[2])
    total_Antwerp = len(data_frames[3])
    total_Bangkok = len(data_frames[4])


    # Calculate total number of data points
    total_data_points_Albany = len(room_type_counts_Albany)
    total_data_points_Athens = len(room_type_counts_Athens)
    total_data_points_Amsterdam = len(room_type_counts_Amsterdam)
    total_data_points_Antwerp = len(room_type_counts_Antwerp)
    total_data_points_Bangkok = len(room_type_counts_Bangkok)


    # Calculate percentages of each room type
    room_type_percentages_Albany = data_frames[0]['room_type'].value_counts(normalize=True) * 100
    room_type_percentages_Athens = data_frames[1]['room_type'].value_counts(normalize=True) * 100
    room_type_percentages_Amsterdam = data_frames[2]['room_type'].value_counts(normalize=True) * 100
    room_type_percentages_Antwerp = data_frames[3]['room_type'].value_counts(normalize=True) * 100
    room_type_percentages_Bangkok = data_frames[4]['room_type'].value_counts(normalize=True) * 100
    return total_Albany, total_Bangkok, total_Antwerp, total_Amsterdam, total_Athens,\
           room_type_counts_Albany, room_type_counts_Athens, room_type_counts_Amsterdam, room_type_counts_Antwerp, room_type_counts_Bangkok,  \
           total_data_points_Albany, total_data_points_Athens, total_data_points_Amsterdam, total_data_points_Antwerp, total_data_points_Bangkok,\
           room_type_percentages_Bangkok, room_type_percentages_Antwerp, room_type_percentages_Amsterdam, room_type_percentages_Athens, room_type_percentages_Albany



def main():
    print(calculate())
    data_frames = load_data()
    # Plotting
    plot_room_type_distribution(data_frames, 'Albany')
    plot_room_type_distribution(data_frames, 'Athens')
    plot_room_type_distribution(data_frames, 'Amsterdam')
    plot_room_type_distribution(data_frames, 'Antwerp')
    plot_room_type_distribution(data_frames, 'Bangkok')

    plot_license_distribution(data_frames, 'Albany')
    plot_license_distribution(data_frames, 'Athens')
    plot_license_distribution(data_frames, 'Amsterdam')
    plot_license_distribution(data_frames, 'Antwerp')
    plot_license_distribution(data_frames, 'Bangkok')

    # Mapping
    create_map(data_frames,'Albany', 'AlbanyMap.html' )
    create_map(data_frames,'Athens', 'AthensMap.html' )
    create_map(data_frames,'Amsterdam', 'AmsterdamMap.html' )
    create_map(data_frames,'Antwerp', 'AntwerpMap.html' )
    create_map(data_frames,'Bangkok', 'BangkokMap.html' )

    calculate()

    locations = ['Albany', 'Athens', 'Amsterdam', 'Antwerp', 'Bangkok']

    # Base directory where the files are stored
    base_path = '/Users/lyk-dar/IdeaProjects/AirBnb Analysis'

    # Paths to map files for each location
    maps = [f'{base_path}/{loc}Map.html' for loc in locations]

    # Assuming two charts per location for simplicity
    charts = [[
        f'{base_path}/{loc}_room_type_distribution.png',
        f'{base_path}/{loc}_license_distribution.png'
    ] for loc in locations]

    app = QApplication(sys.argv)
    window = DataVisualizationApp(locations, maps, charts)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
