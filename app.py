from enum import Enum
class Operation(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

operation_dict = {
    Operation.ADD: add,
    Operation.SUBTRACT: subtract,
    Operation.MULTIPLY: multiply,
    Operation.DIVIDE: divide
}

# Main function
def main():
    while True:
        user_input = input("Enter operation (add/subtract/multiply/divide/quit): ")

        if user_input == "quit":
            break
        elif user_input in {op.value for op in Operation}:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Get the corresponding Enum value and call the corresponding function
            operation_enum = next(op for op in Operation if op.value == user_input)
            operation_function = operation_dict[operation_enum]
            result = operation_function(num1, num2)
            print("Result:", result)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
