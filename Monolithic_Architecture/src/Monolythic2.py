# main.py (Monolithic Application)
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"


if __name__ == "__main__":
    calculator = Calculator()

    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter operation number: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = calculator.add(num1, num2)
    elif choice == "2":
        result = calculator.subtract(num1, num2)
    elif choice == "3":
        result = calculator.multiply(num1, num2)
    elif choice == "4":
        result = calculator.divide(num1, num2)
    else:
        result = "Invalid choice"

    print("Result: ", result)
