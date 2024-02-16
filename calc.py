#!/usr/bin/python3
"""calculator class"""


class Calc:
    """calculator that adds subtracts, multiplies and divides only"""
    @staticmethod
    def add(a, b):
        """adds two numbers"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """subtracts b from a"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """multiplies two numbers"""
        return a * b

    @staticmethod
    def divide(a, b):
        """divides a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b


def main():
    """main function"""
    print(f"{Calc.add(1,2)}")
    print(f"{Calc.subtract(4,2)}")
    print(f"{Calc.multiply(3,4)}")
    print(f"{Calc.divide(10,2)}")


if __name__ == "__main__":
    main()
