import numpy as np
from PyQt5.QtGui import QColor
import colorsys
def valueToColor(value, minimum, maximum):
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




    def valueToColorRB(self,value, minimum, maximum):
        """
        Map a numeric value to a rainbow color.
        :param value: Numeric value between 0 and 11000.
        :return: QColor corresponding to the value on a rainbow spectrum.
        """
        # Clamp value to be between 0 and 11000
        value = max(minimum, min(value, maximum))

        # Map the value to a hue in the range 0-1
        hue = value / maximum  # This will give a range from 0 (red) to 1 (back to red)

        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Saturation and Value are set to 1 for full color

        # Convert RGB from 0-1 range to 0-255 range
        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        return QColor(r, g, b)


def valueToColor3Point(value, min_value, middle_value, max_value):
    """
    Map a numeric value to a color with a smooth transition between specified minimum, middle, and maximum values.
    :param value: Numeric value.
    :param min_value: Minimum value for color mapping.
    :param middle_value: Middle value for color mapping.
    :param max_value: Maximum value for color mapping.
    :return: QColor corresponding to the value.
    """
    # Define RGB values for colors
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)

    # Clamp the value to be within the specified range
    value = min(max(value, min_value), max_value)

    if value <= middle_value:
        # Map value between min_value and middle_value
        if value <= min_value + (middle_value - min_value) / 2:
            fraction = (value - min_value) / (middle_value - min_value) * 2
            r = int(red[0] + (yellow[0] - red[0]) * fraction)
            g = int(red[1] + (yellow[1] - red[1]) * fraction)
            b = int(red[2] + (yellow[2] - red[2]) * fraction)
        else:
            fraction = (value - min_value - (middle_value - min_value) / 2) / (middle_value - min_value) * 2
            r = int(yellow[0] + (green[0] - yellow[0]) * fraction)
            g = int(yellow[1] + (green[1] - yellow[1]) * fraction)
            b = int(yellow[2] + (green[2] - yellow[2]) * fraction)
    else:
        # Map value between middle_value and max_value
        if value <= middle_value + (max_value - middle_value) / 2:
            fraction = (value - middle_value) / (max_value - middle_value) * 2
            r = int(green[0] + (yellow[0] - green[0]) * fraction)
            g = int(green[1] + (yellow[1] - green[1]) * fraction)
            b = int(green[2] + (yellow[2] - green[2]) * fraction)
        else:
            fraction = (value - middle_value - (max_value - middle_value) / 2) / (max_value - middle_value) * 2
            r = int(yellow[0] + (red[0] - yellow[0]) * fraction)
            g = int(yellow[1] + (red[1] - yellow[1]) * fraction)
            b = int(yellow[2] + (red[2] - yellow[2]) * fraction)

    return QColor(r, g, b)

def valueToColorInverse(value, minimum, maximum):
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
        r = red[0] + (orange[0] - red[0]) * fraction
        g = red[1] + (orange[1] - red[1]) * fraction
        b = red[2] + (orange[2] - red[2]) * fraction
    elif value < thresholds[2]:
        # Interpolate between yellow and orange
        fraction = (value - thresholds[1]) / (thresholds[2] - thresholds[1])
        r = orange[0] + (yellow[0] - orange[0]) * fraction
        g = orange[1] + (yellow[1] - orange[1]) * fraction
        b = orange[2] + (yellow[2] - orange[2]) * fraction
    else:
        # Interpolate between orange and red
        fraction = (value - thresholds[2]) / (thresholds[3] - thresholds[2])
        r = yellow[0] + (green[0] - yellow[0]) * fraction
        g = yellow[1] + (green[1] - yellow[1]) * fraction
        b = yellow[2] + (green[2] - yellow[2]) * fraction

    return QColor(int(r), int(g), int(b))