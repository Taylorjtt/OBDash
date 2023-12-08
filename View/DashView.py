

import customtkinter
import tkinter as tk
from View.Colors import Colors
from View.LabelFactory import getLargeLabel, getLargeData
from app import App

row_padding = 20
top_padding = 40
class DashView:
    def __init__(self):

        self.dataPanel = customtkinter.CTkFrame(App.root, width=1910, height=1070, fg_color=Colors.bgcolor)

        self.oilPressureLabel = getLargeLabel(self.dataPanel,"OILP")
        self.oilTempLabel = getLargeLabel(self.dataPanel, "OILT")
        self.waterTempLabel = getLargeLabel(self.dataPanel, "WTEMP")

        self.oilPressureData = getLargeData(self.dataPanel,"50 PSI")
        self.oilTempData = getLargeData(self.dataPanel, "210 °F")
        self.waterTempData = getLargeData(self.dataPanel, "210 °F")

        self.speedLabel = getLargeLabel(self.dataPanel, "SPEED")
        self.RPMLabel = getLargeLabel(self.dataPanel, "RPM")
        self.FuelLevelLabel = getLargeLabel(self.dataPanel, "FUEL")

        self.speedData = getLargeData(self.dataPanel, "100 MPH")
        self.RPMData = getLargeData(self.dataPanel, "4.5K")
        self.FuelLevelData = getLargeData(self.dataPanel, "30%")


        self.voltsLabel = getLargeLabel(self.dataPanel, "VOLTS")
        self.AFRLabel = getLargeLabel(self.dataPanel, "AFR")
        self.GearLabel = getLargeLabel(self.dataPanel, "GEAR")

        self.voltsData = getLargeData(self.dataPanel, "12.2 V")
        self.AFRData= getLargeData(self.dataPanel, "19.3")
        self.GearData = getLargeData(self.dataPanel, "2")


        App.root.grid_rowconfigure(0, weight=1)
        App.root.grid_rowconfigure(3, weight=1)

        self.dataPanel.grid_propagate(False)
        self.dataPanel.grid(column=0, row=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.dataPanel.grid_columnconfigure(0, weight=1)
        self.dataPanel.grid_columnconfigure(1, weight=1)
        self.dataPanel.grid_columnconfigure(2, weight=1)


        self.gridLabels()
        self.gridData()

        self.dataPanel.grid(column=0, row=2)

    def gridLabels(self):
        self.oilPressureLabel.grid(column=0, row=1,pady=(top_padding,0))
        self.oilTempLabel.grid(column=1, row=1,pady=(top_padding,0))
        self.waterTempLabel.grid(column=2, row=1,pady=(top_padding,0))

        self.speedLabel.grid(column=0, row=3)
        self.RPMLabel.grid(column=1, row=3)
        self.FuelLevelLabel.grid(column=2, row=3)

        self.voltsLabel.grid(column=0, row=5)
        self.AFRLabel.grid(column=1, row=5)
        self.GearLabel.grid(column=2, row=5)

    def gridData(self):
        self.oilPressureData.grid(column=0, row=2, pady=(0,row_padding))
        self.oilTempData.grid(column=1, row=2, pady=(0,row_padding))
        self.waterTempData.grid(column=2, row=2, pady=(0,row_padding))

        self.speedData.grid(column=0, row=4, pady=(0,row_padding))
        self.RPMData.grid(column=1, row=4, pady=(0,row_padding))
        self.FuelLevelData.grid(column=2, row=4, pady=(0,row_padding))

        self.voltsData.grid(column=0, row=6, pady=(0,row_padding))
        self.AFRData.grid(column=1, row=6, pady=(0,row_padding))
        self.GearData.grid(column=2, row=6, pady=(0,row_padding))


    def setData(self, data):


        sensors = {
            'oil_pressure': self.oilPressureData,
            'oil_temperature': self.oilTempData,
            'water_temperature': self.waterTempData,
            'speed': self.speedData,
            'rpm': self.RPMData,
            'fuel_level': self.FuelLevelData,
            'battery_volts': self.voltsData,
            'air_fuel_ratio': self.AFRData,
            'selected_gear': self.GearData  # Note: Not all vehicles support this
        }
        print(data)
        for s, d in data.items():
            print(d)
            if d is None:
                sensors[s].configure(text="0.0")
            else:
                sensors[s].configure(text=d.magnitude)



