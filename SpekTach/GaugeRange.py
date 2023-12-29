class GaugeRange:
    def __init__(self):
        self.equations = []

    def add_linear_equation(self, equation):
        self.equations.append(equation)

    def find_linear_equation(self, x):
        for equation in self.equations:
            if equation.point1[0] <= x <= equation.point2[0] or equation.point2[0] <= x <= equation.point1[0]:
                return equation
        raise ValueError("No linear equation found for the given input value. " + str(x))
    def find_linear_equation_inv(self, y):
        for equation in self.equations:
            if equation.point1[1] <= y <= equation.point2[1] or equation.point2[1] <= y <= equation.point1[1]:
                return equation
        raise ValueError("No linear equation found for the given input value."+ str(y))
    def get_y(self, x):
        equation = self.find_linear_equation(x)
        return equation.get_y(x)
    def get_inv(self, x):
        equation = self.find_linear_equation_inv(x)
        return equation.get_inverse().get_y(x)