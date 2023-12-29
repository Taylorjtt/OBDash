import numpy as np

from Gauge import Gauge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QPalette, QPainter, QPainterPath,QBitmap,QScreen
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt, QPixmap

from ColorUtils import valueToColor, valueToColor3Point
from LinearEquation import LinearEquation
from GaugeRange import GaugeRange
from SmallGauge import SmallGauge


class VoltGauge(SmallGauge):
    def __init__(self,parent, xpos,ypos,width, height, needle, face, led):
        super().__init__(parent, xpos,ypos,width, height, needle, face, led)
        self.NeedleLabel.raise_()
        point1 = (0, 0)
        point2 = (24, 280)
        equation1 = LinearEquation(point1, point2)

        self.gauge_range = GaugeRange()
        self.gauge_range.add_linear_equation(equation1)

        self.colors = []
        self.calculateColors()

        print(self.colors)
    def setValue(self, value):
        if value is None:
            value = 0
        angle = self.valueToAngle(value)
        self.setNeedleAngle(angle)
        self.setColor(angle)

    def valueToAngle(self, value):
        return self.gauge_range.get_y(value)

    def angleToValue(self, angle):
        return self.gauge_range.get_inv(angle)

    def valueToColor(self, value):
         return valueToColor3Point(value, 11.8, 12.5,14.5)


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

