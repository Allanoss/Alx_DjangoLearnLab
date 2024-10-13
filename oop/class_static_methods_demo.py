class Calculator:
    """A class to perform basic arithmetic operations."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Testing the Calculator class
#if __name__ == "__main__":
#    # Using the static method
#    sum_result = Calculator.add(5, 10)
#    print(f"Sum: {sum_result}")  # Output: Sum: 15
#
#    # Using the class method
#    product_result = Calculator.multiply(5, 10)
#    print(f"Product: {product_result}")  # Output: Product: 50
