import numpy as np

from Gauge import Gauge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QPalette, QPainter, QPainterPath,QBitmap,QScreen
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt, QPixmap

from ColorUtils import valueToColor
from LinearEquation import LinearEquation
from GaugeRange import GaugeRange
from SmallGauge import SmallGauge


class WaterTempGauge(SmallGauge):
    def __init__(self,parent, xpos,ypos,width, height, needle, face, led):
        super().__init__(parent, xpos,ypos,width, height, needle, face, led)
        self.NeedleLabel.raise_()
        point1 = (100, 0)
        point2 = (160, 50)
        equation1 = LinearEquation(point1, point2)

        point1 = (160, 50)
        point2 = (240, 230)
        equation2 = LinearEquation(point1, point2)

        point1 = (240, 230)
        point2 = (300, 280)
        equation3 = LinearEquation(point1, point2)

        self.gauge_range = GaugeRange()
        self.gauge_range.add_linear_equation(equation1)
        self.gauge_range.add_linear_equation(equation2)
        self.gauge_range.add_linear_equation(equation3)

        self.colors = []
        self.calculateColors()

        print(self.colors)
    def setValue(self, value):
        if value is None:
            value = 100
        angle = self.valueToAngle(value)
        self.setNeedleAngle(angle)
        self.setColor(angle)

    def valueToAngle(self, value):
        return self.gauge_range.get_y(value)

    def angleToValue(self, angle):
        return self.gauge_range.get_inv(angle)

    def valueToColor(self, value):
         return valueToColor(value, 100, 220)


    def setColor(self, angle):
        differences = np.abs(self.colorAngles - angle)
        closest_index = np.argmin(differences)
        # Create a new pixmap with the updated image
        new_pixmap = self.colors[closest_index]
        # Set the buffer pixmap to NeedleLabel
        self.LED.setPixmap(new_pixmap)

    def calculateColors(self):
        for angle in self.colorAngles:
            if angle <= 280:
                pixmap = QtGui.QPixmap.fromImage(ImageQt(self.ledImage))
                pixmap.fill(self.valueToColor(self.angleToValue(angle)))
                self.colors.append(pixmap)

