class calculator:
    """
  A simple calculator class that performs basic arithmetic operations.
  """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    """
    Initializes the calculator with two numbers.

    Args:
      num1: The first number.
      num2: The second number.
    """
    def addition(self):
        return self.num1 + self.num2
    """
    Adds the two numbers and returns the result.
    """
    def subtraction(self):
        return self.num1 - self.num2
    """
    Subtracts the two numbers and returns the result.
    """
    def multiplication(self):
        return self.num1*self.num2
    """
    Multiplies the two numbers and returns the result.
    """
    def division(self):
        return self.num1/self.num2
    """
    Divides the two numbers and returns the result.
    """
    