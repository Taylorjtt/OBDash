import numpy as np

from Gauge import Gauge
import os
from PIL.ImageQt import ImageQt, QPixmap
class LargeGauge(Gauge):
    needleImages = []
    def __init__(self,parent, xpos,ypos,width, height, needle, face, led):
        super().__init__(parent, xpos,ypos,width, height, needle, face, led)
        if not LargeGauge.needleImages:
            self.createCache()

    def createCache(self):
        print("Creating Cache")
        for angle in self.angles:
            if not os.path.exists("/home/dash/OBDash/SpekTach/Cache/large_needle_" + str(angle)+".png"):
                print("Angle Image Not Found")
                p = self.rotateImage(self.needle, angle)
                LargeGauge.needleImages.append(p)
                p.save("/home/dash/OBDash/SpekTach/Cache/large_needle_" + str(angle)+".png", "PNG")
                print("Done Creating " + str(angle))
            else:
                print("Angle Image Found")
                LargeGauge.needleImages.append(QPixmap("/home/dash/OBDash/SpekTach/Cache/large_needle_" + str(angle)+".png"))
                print("Done Loading " + str(angle))
    def setNeedleAngle(self, angle):
        differences = np.abs(self.angles - angle)
        closest_index = np.argmin(differences)
        # Create a new pixmap with the updated image
        new_pixmap = LargeGauge.needleImages[closest_index]
        # Set the buffer pixmap to NeedleLabel
        self.NeedleLabel.setPixmap(new_pixmap)
        self.NeedleLabel.raise_()