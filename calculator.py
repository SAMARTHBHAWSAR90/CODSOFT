"""

Internship Task - Python Programming
Task: Build a Command-Line Calculator with Basic Arithmetic Operations

Description:
This Python program allows the user to perform basic arithmetic operations (Addition, Substraction, Multiplication, and Division) by inputting two numbers and selecting the desired operation. The code includes error handling for invalid inputs and divide-by-zero cases.

Samarth Bhawsar
"""

class SimpleCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        try:
            self.num1 = float(input("Enter the first number: "))
            self.num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return False    
        return True
    
    def operate(self, choice):
        if choice == "+":
            return self.num1 + self.num2
        elif choice == "-":
            return self.num1 - self.num2
        elif choice == "*":
            return self.num1 * self.num2
        elif choice == "/":
            if self.num2 == 0:
                return "Error! Division by zero is not allowed."
            return self.num1 / self.num2
        else:
            return "Invalid Operation!"
        
    def start(self):
        print("Welcome to the Simple Calculator!")
        print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

        if not self.get_input():
            return
        
        op = input("Choose an operation:").strip()
        result = self.operate(op)
        print(f"The result of {self.num1} {op} {self.num2} is: {result}")

if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.start()
        