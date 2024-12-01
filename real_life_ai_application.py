def simple_calculator():
    # Ask for user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the operation using decision-making (AI-like logic)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    # Display the result
    print("Result: ", result)

# Run the calculator
simple_calculator()
