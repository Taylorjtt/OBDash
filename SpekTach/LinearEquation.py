class LinearEquation:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.slope = self.calculate_slope()
        self.intercept = self.calculate_intercept()

    def calculate_slope(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        if x1 == x2:
            raise ValueError("Cannot create a linear equation with vertical line (infinite slope).")
        return (y2 - y1) / (x2 - x1)

    def calculate_intercept(self):
        x1, y1 = self.point1
        return y1 - self.slope * x1

    def get_y(self, x):
        return self.slope * x + self.intercept

    def get_inverse(self):
        if self.slope == 0:
            raise ValueError("Cannot find the inverse equation for a horizontal line (slope is zero).")
        inverse_slope = 1 / self.slope
        inverse_intercept = -self.intercept / self.slope
        return LinearEquation((0, inverse_intercept), (1, inverse_slope + inverse_intercept))