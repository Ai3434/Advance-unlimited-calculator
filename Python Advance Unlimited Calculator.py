def calculate():
  """Performs calculations based on user input, handling multiple operations.

  Returns:
      float: The final result.
  """

  result = None
  while True:
    try:
      if result is None:
        operand = float(input("Enter a number: "))
        result = operand
      else:
        operator = input("Enter an operator (+, -, *, /) or '.' to quit: ").lower().strip()
        if operator == '.':
          return result  # Return final result
        operand2 = float(input(f"Enter the second number for {operator}: "))
        result = calculate_operation(result, operator, operand2)
        print(f"Result: {result}")
    except ValueError:
      print("Invalid input. Please enter a number.")

def calculate_operation(num1, operator, num2):
  """Performs a specific calculation based on the operators
  """

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return num1  # Return current result for further calculations
    else:
      return num1 / num2
  else:
    print("Invalid operator. Please use +, -, *, or /.")
    return num1  # Return current result for further calculations

if __name__ == "__main__":
  result = calculate()
  print("Final result:", result)
print("This program is created by Muhammad Hamza")  
