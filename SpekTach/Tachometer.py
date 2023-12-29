import numpy as np

from Gauge import Gauge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QPalette, QPainter, QPainterPath,QBitmap,QScreen
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt, QPixmap

from ColorUtils import valueToColor
from LargeGauge import LargeGauge


class Tach(LargeGauge):
    def __init__(self,parent, xpos,ypos,width, height, needle, face, led, RLs, glass):

        super().__init__(parent, xpos,ypos,width, height, needle, face, led)
        self.RevLights = []
        for rl in RLs:
            revLight = QtWidgets.QLabel(self.centralwidget)
            revLight.setGeometry(QtCore.QRect(xpos, ypos, width, height))
            revLight.setPixmap(QtGui.QPixmap(rl))
            revLight.setText("")
            self.RevLights.append(revLight)
        self.Glass = QtWidgets.QLabel(self.centralwidget)
        self.Glass.setGeometry(QtCore.QRect(xpos, ypos, width, height))
        self.Glass.setText("")
        self.Glass.setPixmap(QtGui.QPixmap(glass))
        self.NeedleLabel.raise_()
        self.colors = []
        self.calculateColors()
        print(self.colors)



    def setRPM(self, rpm):
        if rpm == None:
            rpm = 0
        angle = rpm/1000*28
        self.setNeedleAngle(angle)
        self.setColor(angle)
        #self.setColorOfNonTransparentPixels(self.Lettering,self.valueToColorRB(rpm))
        #self.update_circles_based_on_rpm(rpm)

    def setColor(self, angle):
        differences = np.abs(self.colorAngles - angle)
        closest_index = np.argmin(differences)

        # Create a new pixmap with the updated image
        new_pixmap = self.colors[closest_index]

        # Set the buffer pixmap to NeedleLabel
        self.LED.setPixmap(new_pixmap)

    def calculateColors(self):
        for angle in self.colorAngles:
            pixmap = QtGui.QPixmap.fromImage(ImageQt(self.ledImage))
            pixmap.fill(valueToColor((1000*angle)/28, 0, 6000))
            self.colors.append(pixmap)

    def valueToColor(self,value, minimum, maximum):
        """
        Map a numeric value to a color.
        :param value: Numeric value between 0 and 5000 (5000+ will also be mapped to red).
        :return: QColor corresponding to the value.
        """
        # Clamp value to be between 0 and 5000
        value = min(max(value, minimum), maximum)

        # Define RGB values for colors
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        orange = (255, 165, 0)
        red = (255, 0, 0)

        thresholds = np.linspace(minimum, maximum, 4)
        if value < thresholds[1]:
            # Interpolate between green and yellow
            fraction = value / thresholds[1]
            r = green[0] + (yellow[0] - green[0]) * fraction
            g = green[1] + (yellow[1] - green[1]) * fraction
            b = green[2] + (yellow[2] - green[2]) * fraction
        elif value < thresholds[2]:
            # Interpolate between yellow and orange
            fraction = (value - thresholds[1]) / (thresholds[2] - thresholds[1])
            r = yellow[0] + (orange[0] - yellow[0]) * fraction
            g = yellow[1] + (orange[1] - yellow[1]) * fraction
            b = yellow[2] + (orange[2] - yellow[2]) * fraction
        else:
            # Interpolate between orange and red
            fraction = (value - thresholds[2]) / (thresholds[3] - thresholds[2])
            r = orange[0] + (red[0] - orange[0]) * fraction
            g = orange[1] + (red[1] - orange[1]) * fraction
            b = orange[2] + (red[2] - orange[2]) * fraction

        return QColor(int(r), int(g), int(b))
