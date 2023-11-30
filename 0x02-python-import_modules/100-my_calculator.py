#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    # Import necessary functions and modules
    from calculator_1 import add, sub, mul, div
    import sys

    # Check the number of command-line arguments
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Define a dictionary mapping operators to functions
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the operator is valid
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Extract operands and operator from command-line arguments
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    # Perform the calculation and display the result
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
