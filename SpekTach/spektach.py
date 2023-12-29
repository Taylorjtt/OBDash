# -*- coding: utf-8 -*-

import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from Gauge import Gauge

from SensorModel import initConnection, sample_fast_sensor_values, sampleMedSensorValues, sampleSlowSensorValues
from TimingGauge import TimingGauge
from VoltGauge import VoltGauge
from WaterTempGauge import WaterTempGauge
from FuelGauge import FuelGauge
from Tachometer import Tach

width = 1920
height = 1080
midpoint = 455

up = 0
rootPath = "/home/dash/OBDash/SpekTach/Images/"
class Ui_SpekTach(object):

    def __init__(self):
        self.slowData = None
        self.medData = None
        self.fastData = None
        self.current_angle = None
        self.fuel_percent_start_time = None
        self.fuelPercentTimer = None
        self.timing_advance_start_time = None
        self.timingAdvanceTimer = None
        self.battery_volts_start_time = None
        self.batteryVoltageTimer = None
        self.water_temp_start_time = None
        self.WaterTempTimer = None
        self.tach_start_time = None
        self.TachTimer = None
        self.carbonFiber = None
        self.centralwidget = None
        self.timingAdv = None
        self.fuelPercentage = None
        self.batteryLevelGauge = None
        self.waterTempGauge = None
        self.smallGauges = None
        self.tach = None

    def setupUi(self, SpekTach):
        SpekTach.setObjectName("SpekTach")
        SpekTach.resize(width, height)
        self.setGeometry(0, 0, width, height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(SpekTach)
        self.centralwidget.setObjectName("centralwidget")

        initConnection()
        self.fastSensorSampleTimer = QtCore.QTimer(self.centralwidget)
        self.fastSensorSampleTimer.timeout.connect(self.updateFastSensors)
        self.fastSensorSampleTimer.start()


        self.medSensorSampleTimer = QtCore.QTimer(self.centralwidget)
        self.medSensorSampleTimer.timeout.connect(self.updateMedSensors)
        self.medSensorSampleTimer.start(1000)


        self.slowSensorSampleTimer = QtCore.QTimer(self.centralwidget)
        self.slowSensorSampleTimer.timeout.connect(self.updateSlowSensors)
        self.slowSensorSampleTimer.start(10000)

        RLs = [rootPath + "rl1.png",rootPath + "rl2.png",rootPath + "rl3.png",rootPath + "rl4.png",rootPath + "rl5.png",
               rootPath + "rl6.png",rootPath + "rl7.png",]


        self.tach = Tach(self.centralwidget, 439 ,19,1042, 1042, rootPath + "needle.png",rootPath + "tach_face.png" , rootPath + "LED.png",RLs,rootPath + "glass.png")

        self.smallGauges = []
        self.waterTempGauge = WaterTempGauge(self.centralwidget, 21 ,19,420, 424, rootPath + "small_gauge_needle.png",rootPath + "water_temp_face.png" , rootPath + "small_gauge_led.png")

        self.batteryLevelGauge = VoltGauge(self.centralwidget, 1478, 20, 420, 424, rootPath + "small_gauge_needle.png",
                                    rootPath + "batt_voltage_face.png", rootPath + "small_gauge_led.png")

        self.fuelPercentage = FuelGauge(self.centralwidget, 1478, 637, 420, 424, rootPath + "small_gauge_needle.png",
                                    rootPath + "fuel_level_face.png", rootPath + "small_gauge_led.png")

        self.timingAdv = TimingGauge(self.centralwidget, 21, 637, 420, 424, rootPath + "small_gauge_needle.png",
                                    rootPath + "timing_advance_face.png", rootPath + "small_gauge_led.png")
        self.smallGauges.append(self.waterTempGauge)
        self.smallGauges.append(self.batteryLevelGauge)
        self.smallGauges.append(self.fuelPercentage)
        self.smallGauges.append(self.timingAdv)

        self.carbonFiber = QtWidgets.QLabel(self.centralwidget)
        self.carbonFiber.setObjectName("carbonFiber")
        self.carbonFiber.setEnabled(True)
        self.carbonFiber.setGeometry(QtCore.QRect(0, 0, width, height))
        self.carbonFiber.setText("")
        self.carbonFiber.setPixmap(QtGui.QPixmap(rootPath + "background.png"))

        self.centralwidget.lower()
        self.showFullScreen()

        SpekTach.setCentralWidget(self.centralwidget)
        # Timer setup
        self.TachTimer = QtCore.QTimer(self.centralwidget)
        self.tach_start_time = None
        self.TachTimer.timeout.connect(self.update_tach)
        self.TachTimer.start()

        self.WaterTempTimer = QtCore.QTimer(self.centralwidget)
        self.WaterTempTimer.timeout.connect(self.update_water_temp)
        self.water_temp_start_time = None
        self.WaterTempTimer.start(10000)

        self.batteryVoltageTimer = QtCore.QTimer(self.centralwidget)
        self.batteryVoltageTimer.timeout.connect(self.update_batt_voltage)
        self.battery_volts_start_time = None
        self.batteryVoltageTimer.start(1000)

        self.timingAdvanceTimer = QtCore.QTimer(self.centralwidget)
        self.timingAdvanceTimer.timeout.connect(self.update_timing_adv)
        self.timing_advance_start_time = None
        self.timingAdvanceTimer.start()


        self.fuelPercentTimer = QtCore.QTimer(self.centralwidget)
        self.fuelPercentTimer.timeout.connect(self.update_fuel_percent)
        self.fuel_percent_start_time = None
        self.fuelPercentTimer.start(10000)

        self.current_angle = 0
        self.fastData = []
        self.tach.LED.lower()

        self.retranslateUi(SpekTach)
        QtCore.QMetaObject.connectSlotsByName(SpekTach)



    def retranslateUi(self, SpekTach):
        _translate = QtCore.QCoreApplication.translate
        SpekTach.setWindowTitle(_translate("SpekTach", "MainWindow"))

    def updateFastSensors(self):
        self.fastData = sample_fast_sensor_values()
    def updateMedSensors(self):
        self.medData = sampleMedSensorValues()
    def updateSlowSensors(self):
        self.slowData = sampleSlowSensorValues()

    def update_tach(self):
        # seconds = 10
        # if self.tach_start_time is None:
        #     self.tach_start_time = time.time()
        # elapsed_time = (time.time() - self.tach_start_time) % seconds * 2  # Repeat every 14 seconds
        # if elapsed_time <= seconds:
        #     # First 7 seconds: value goes from 0 to 11000
        #     value = (elapsed_time / seconds) * 11000
        # else:
        #     # Next 7 seconds: value goes from 11000 back to 0
        #     value = ((seconds* 2 - elapsed_time) / seconds) * 11000
        print(self.fastData)
        if self.fastData['rpm'] is not None:
            self.tach.setRPM(self.fastData['rpm'].magnitude)
        else:
            self.tach.setRPM(0)





    def update_water_temp(self):
        pass
        # seconds = 15
        #
        # if self.water_temp_start_time is None:
        #     self.water_temp_start_time = time.time()
        #
        # elapsed_time = (time.time() - self.water_temp_start_time) % seconds * 2  # Repeat every 14 seconds
        #
        # if elapsed_time <= seconds:
        #     waterTempAngle = (elapsed_time / seconds) * 300
        # else:
        #     waterTempAngle = ((seconds * 2 - elapsed_time) / seconds) * 300

        if self.slowData['water_temperature'] is not None:
            self.waterTempGauge.setValue(self.slowData['water_temperature'].magnitude)
        else:
            self.waterTempGauge.setValue(100)


    def update_timing_adv(self):
        pass
        # seconds = 15
        # if self.timing_advance_start_time is None:
        #     self.timing_advance_start_time = time.time()
        #
        # elapsed_time = (time.time() - self.timing_advance_start_time) % seconds * 2  # Repeat every 14 seconds
        #
        # if elapsed_time <= seconds:
        #     timingAdvAngle = (elapsed_time / seconds) * 50
        # else:
        #     timingAdvAngle = ((seconds * 2 - elapsed_time) / seconds) * 50
        if self.fastData['timing_advance'] is not None:
            self.timingAdv.setValue(self.fastData['timing_advance'].magnitude)
        else:
            self.timingAdv.setValue(0)


    def update_fuel_percent(self):
        pass
        # seconds = 15
        # if self.fuel_percent_start_time is None:
        #     self.fuel_percent_start_time = time.time()
        #
        # elapsed_time = (time.time() - self.fuel_percent_start_time) % seconds * 2  # Repeat every 14 seconds
        #
        # if elapsed_time <= seconds:
        #     fuelPercentAngle = (elapsed_time / seconds) * 100
        # else:
        #     fuelPercentAngle = ((seconds * 2 - elapsed_time) / seconds) * 100

        if self.slowData['fuel_level'] is not None:
            self.fuelPercentage.setValue(self.slowData['fuel_level'].magnitude)
        else:
            self.fuelPercentage.setValue(0)

    def update_batt_voltage(self):
        pass
        # seconds = 15
        # if self.battery_volts_start_time is None:
        #     self.battery_volts_start_time = time.time()
        #
        # elapsed_time = (time.time() - self.battery_volts_start_time) % seconds * 2  # Repeat every 14 seconds
        #
        # if elapsed_time <= seconds:
        #     batt_voltage = (elapsed_time / seconds) * 24
        # else:
        #     batt_voltage = ((seconds * 2 - elapsed_time) / seconds) * 24
        if self.medData['battery_volts'] is not None:
            self.batteryLevelGauge.setValue(self.medData['battery_volts'].magnitude)
        else:
            self.batteryLevelGauge.setValue(0)



    # def update_circles_based_on_rpm(self, rpm):
    #     state = self.calculate_state(rpm)
    #
    #     current_color_index = state // 7
    #     num_lit = state % 7  # Determines how many circles to light up
    #
    #     for i, label in enumerate(self.circle_labels):
    #         if i < num_lit:
    #             self.setColorOfNonTransparentPixels(self.circle_labels[i], self.colors[current_color_index])
    #         else:
    #             # If 'off' state, set to gray or another 'off' color
    #             self.setColorOfNonTransparentPixels(self.circle_labels[i], self.colors[0])
    # def calculate_state(self, rpm):
    #     rpm = max(1000, min(rpm, 5000))  # Clamp RPM value
    #     return int(((rpm - 1000) / 4000) * 22)  # Map RPM to a state between 0 and 20
    #
    #




class MyWindow(QtWidgets.QMainWindow, Ui_SpekTach):
    def __init__(self):
        super().__init__()
        self.setupUi(self)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    # SpekTach.show()
    sys.exit(app.exec_())
