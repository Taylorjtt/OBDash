# -*- coding: utf-8 -*-
import colorsys
import time
from cmath import rect

import numpy as np
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt, QPixmap
# Form implementation generated from reading ui file '.\spektach.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QPalette

width = 1500
class Ui_SpekTach(object):
    def setupUi(self, SpekTach):
        SpekTach.setObjectName("SpekTach")
        SpekTach.resize(1500, 1500)
        self.centralwidget = QtWidgets.QWidget(SpekTach)
        self.centralwidget.setObjectName("centralwidget")
        self.Lettering = QtWidgets.QLabel(self.centralwidget)
        self.Lettering.setEnabled(True)
        self.Lettering.setGeometry(QtCore.QRect(0, 0, width, width))
        self.Lettering.setText("")
        self.Lettering.setPixmap(QtGui.QPixmap(".\\Images\\lettering.png"))
        self.Lettering.setObjectName("Lettering")
        self.RL1 = QtWidgets.QLabel(self.centralwidget)
        self.RL1.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1.setText("")
        self.RL1.setPixmap(QtGui.QPixmap(".\\Images\\RL1.png"))
        self.RL1.setObjectName("RL1")
        self.RL1_2 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_2.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_2.setText("")
        self.RL1_2.setPixmap(QtGui.QPixmap(".\\Images\\RL2.png"))
        self.RL1_2.setObjectName("RL1_2")
        self.RL1_3 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_3.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_3.setText("")
        self.RL1_3.setPixmap(QtGui.QPixmap(".\\Images\\RL3.png"))
        self.RL1_3.setObjectName("RL1_3")
        self.RL1_4 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_4.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_4.setText("")
        self.RL1_4.setPixmap(QtGui.QPixmap(".\\Images\\RL4.png"))
        self.RL1_4.setObjectName("RL1_4")
        self.RL1_5 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_5.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_5.setText("")
        self.RL1_5.setPixmap(QtGui.QPixmap(".\\Images\\RL5.png"))
        self.RL1_5.setObjectName("RL1_5")
        self.RL1_6 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_6.setEnabled(True)
        self.RL1_6.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_6.setText("")
        self.RL1_6.setPixmap(QtGui.QPixmap(".\\Images\\RL6.png"))
        self.RL1_6.setObjectName("RL1_6")
        self.RL1_7 = QtWidgets.QLabel(self.centralwidget)
        self.RL1_7.setGeometry(QtCore.QRect(0, 0, width, width))
        self.RL1_7.setText("")
        self.RL1_7.setPixmap(QtGui.QPixmap(".\\Images\\RL7.png"))
        self.RL1_7.setObjectName("RL1_7")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, width, width))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(".\\Images\\face.png"))
        self.Background.setObjectName("Background")
        self.NeedleLabel = QtWidgets.QLabel(self.centralwidget)
        self.NeedleLabel.setGeometry(QtCore.QRect(0, 0, width, width))
        self.NeedleLabel.setText("")
        self.NeedleLabel.setPixmap(QtGui.QPixmap(".\\Images\\needle.png"))
        self.NeedleLabel.setObjectName("NEEDLE")
        self.needle = Image.open(".\\Images\\needle.png")
        self.Glass = QtWidgets.QLabel(self.centralwidget)
        self.Glass.setGeometry(QtCore.QRect(0, 0, width, width))
        self.Glass.setText("")
        self.Glass.setPixmap(QtGui.QPixmap(".\\Images\\glass.png"))
        self.colors = [QColor(128, 128, 128), QColor('green'), QColor('yellow'), QColor('red')]  # QColor objects
        self.circle_labels = [self.RL1,self.RL1_2, self.RL1_3, self.RL1_4, self.RL1_5,self. RL1_6,self.RL1_7]

        self.Glass.setObjectName("Glass")
        self.Lettering.raise_()
        self.Background.raise_()

        self.RL1.raise_()
        self.RL1_2.raise_()
        self.RL1_3.raise_()
        self.RL1_4.raise_()
        self.RL1_5.raise_()
        self.RL1_6.raise_()
        self.RL1_7.raise_()
        self.NeedleLabel.raise_()
        self.Glass.raise_()
        SpekTach.setCentralWidget(self.centralwidget)

        # Timer setup
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.timeout.connect(self.update_needle)
        self.current_angle = 0
        self.start_time = None
        self.timer.start()

        self.retranslateUi(SpekTach)
        QtCore.QMetaObject.connectSlotsByName(SpekTach)

    def retranslateUi(self, SpekTach):
        _translate = QtCore.QCoreApplication.translate
        SpekTach.setWindowTitle(_translate("SpekTach", "MainWindow"))

    def update_needle(self):
        seconds = 20
        if self.start_time is None:
            self.start_time = time.time()

        elapsed_time = (time.time() - self.start_time) % seconds*2  # Repeat every 14 seconds

        if elapsed_time <= seconds:
            # First 7 seconds: value goes from 0 to 11000
            value = (elapsed_time / seconds) * 11000
        else:
            # Next 7 seconds: value goes from 11000 back to 0
            value = ((seconds*2 - elapsed_time) / seconds) * 11000

        self.setRPM(value)

    def update_circles_based_on_rpm(self, rpm):
        state = self.calculate_state(rpm)

        current_color_index = state // 7
        num_lit = state % 7  # Determines how many circles to light up

        for i, label in enumerate(self.circle_labels):
            if i < num_lit:
                self.setColorOfNonTransparentPixels(self.circle_labels[i], self.colors[current_color_index])
            else:
                # If 'off' state, set to gray or another 'off' color
                self.setColorOfNonTransparentPixels(self.circle_labels[i], self.colors[0])
    def calculate_state(self, rpm):
        rpm = max(1000, min(rpm, 5000))  # Clamp RPM value
        return int(((rpm - 1000) / 4000) * 22)  # Map RPM to a state between 0 and 20
    def valueToColorRB(self,value):
        """
        Map a numeric value to a rainbow color.
        :param value: Numeric value between 0 and 11000.
        :return: QColor corresponding to the value on a rainbow spectrum.
        """
        # Clamp value to be between 0 and 11000
        value = max(0, min(value, 11000))

        # Map the value to a hue in the range 0-1
        hue = value / 11000  # This will give a range from 0 (red) to 1 (back to red)

        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Saturation and Value are set to 1 for full color

        # Convert RGB from 0-1 range to 0-255 range
        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        return QColor(r, g, b)

    def valueToColor(self,value):
        """
        Map a numeric value to a color.
        :param value: Numeric value between 0 and 5000 (5000+ will also be mapped to red).
        :return: QColor corresponding to the value.
        """
        # Clamp value to be between 0 and 5000
        value = min(max(value, 0), 5000)

        # Define RGB values for colors
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        orange = (255, 165, 0)
        red = (255, 0, 0)

        # Define thresholds
        thresholds = [0, 2500, 3750, 5000]  # Points of color change

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

    def setNeedleAngle(self, angle):
        new = QtGui.QPixmap.fromImage(ImageQt(self.needle.rotate(-angle)))
        self.NeedleLabel.setPixmap(new)
    def setRPM(self, rpm):
        angle = rpm/1000*28
        self.setNeedleAngle(angle)
        self.setColorOfNonTransparentPixels(self.Lettering,self.valueToColorRB(rpm))
        self.update_circles_based_on_rpm(rpm)

    def setColorOfNonTransparentPixels(self,label, color):
        pixmap = label.pixmap()
        image = pixmap.toImage()
        image = image.convertToFormat(QtGui.QImage.Format_ARGB32)

        ptr = image.bits()
        ptr.setsize(image.byteCount())
        arr = np.array(ptr).reshape(image.height(), image.width(), 4)

        # Only modify pixels that are not fully transparent
        mask = arr[:, :, 3] != 0  # Alpha channel is not zero
        arr[mask, 0] = color.blue()  # Blue

        arr[mask, 1] = color.green()  # Green
        arr[mask, 2] = color.red()  # Red


        # Convert back to QImage and QPixmap
        image = QtGui.QImage(arr.data, image.width(), image.height(), image.bytesPerLine(), QtGui.QImage.Format_ARGB32)
        label.setPixmap(QtGui.QPixmap.fromImage(image))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpekTach = QtWidgets.QMainWindow()

    ui = Ui_SpekTach()

    ui.setupUi(SpekTach)




    SpekTach.show()
    sys.exit(app.exec_())
