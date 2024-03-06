import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt

class DataVisualizationApp(QMainWindow):
    def __init__(self, locations, maps, charts):
        super().__init__()
        self.setWindowTitle("City Data Visualization")
        self.setGeometry(100, 100, 800, 600)  # Adjust size as needed

        self.locations = locations
        self.maps = maps
        self.charts = charts
        self.currentIndex = 0

        self.initUI()
        self.updateNavigationButtons()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QHBoxLayout()

        # Left side: Web view for the map
        self.mapView = QWebEngineView()
        layout.addWidget(self.mapView, 60)

        # Right side: Vertical layout for charts and navigation
        self.rightLayout = QVBoxLayout()
        self.chartsLabels = [QLabel() for _ in self.charts[0]]
        for chartLabel in self.chartsLabels:
            self.rightLayout.addWidget(chartLabel)

        # Navigation buttons
        self.prevButton = QPushButton("Previous")
        self.nextButton = QPushButton("Next")
        self.prevButton.clicked.connect(self.prevLocation)
        self.nextButton.clicked.connect(self.nextLocation)
        self.rightLayout.addWidget(self.prevButton)
        self.rightLayout.addWidget(self.nextButton)

        layout.addLayout(self.rightLayout, 40)
        centralWidget.setLayout(layout)

        self.loadLocationData(self.currentIndex)

    def loadLocationData(self, index):
        # Load the map
        mapPath = os.path.abspath(self.maps[index])
        self.mapView.load(QUrl.fromLocalFile(mapPath))

        # Load the charts
        for chartLabel, chartPath in zip(self.chartsLabels, self.charts[index]):
            chartFullPath = os.path.abspath(chartPath)
            if os.path.exists(chartFullPath):
                pixmap = QPixmap(chartFullPath)
                chartLabel.setPixmap(pixmap.scaled(400, 300, aspectRatioMode=Qt.KeepAspectRatio))  # You can adjust scaling as needed
            else:
                chartLabel.setText(f"Chart not found: {chartPath}")

        self.setWindowTitle(f"City Data Visualization - {self.locations[index]}")
        self.updateNavigationButtons()

    def prevLocation(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            self.loadLocationData(self.currentIndex)

    def nextLocation(self):
        if self.currentIndex < len(self.locations) - 1:
            self.currentIndex += 1
            self.loadLocationData(self.currentIndex)

    def updateNavigationButtons(self):
        self.prevButton.setEnabled(self.currentIndex > 0)
        self.nextButton.setEnabled(self.currentIndex < len(self.locations) - 1)