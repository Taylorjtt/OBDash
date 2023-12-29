import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import colorsys
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt, QPixmap





class Gauge(object):

    def __init__(self,parent, xpos,ypos,width, height, needle, face, led):
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.LED = QtWidgets.QLabel(self.centralwidget)
        self.LED.setEnabled(True)
        self.LED.setGeometry(QtCore.QRect(xpos, ypos, width, height))
        self.LED.setText("")
        self.LED.setPixmap(QtGui.QPixmap(led))
        self.LED.setObjectName("LED")
        self.ledImage = Image.open(led)
        self.face = QtWidgets.QLabel(self.centralwidget)
        self.face.setEnabled(True)
        self.face.setGeometry(QtCore.QRect(xpos, ypos,width, height))
        self.face.setText("")
        self.face.setPixmap(QtGui.QPixmap(face))
        self.face.setObjectName("Face")

        self.NeedleLabel = QtWidgets.QLabel(self.centralwidget)
        self.NeedleLabel.setGeometry(QtCore.QRect(xpos, ypos,width, height))
        self.NeedleLabel.setText("")
        self.NeedleLabel.setPixmap(QtGui.QPixmap(needle))
        self.NeedleLabel.setObjectName("NEEDLE")
        print(needle)
        self.needle = Image.open(needle)


        self.angles = np.arange(0, 360, 2)
        self.colorAngles = np.arange(0, 360, 10)



        self.LED.raise_()
        self.face.raise_()
        self.NeedleLabel.raise_()

        self.buffer_pixmap = QPixmap(self.NeedleLabel.size())
        self.buffer_pixmap.fill(QtCore.Qt.transparent)




    def rotateImage(self, image, angle):
        return QtGui.QPixmap.fromImage(ImageQt(self.needle.rotate(-angle)))











