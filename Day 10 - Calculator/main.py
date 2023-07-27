from art import logo 
from replit import clear

# Add
def add(n1, n2):
  return n1 + n2
  
# Subtract
def subtract(n1, n2):
  return n1 - n2
  
# Multiply
def multiply(n1, n2):
  return n1 * n2
  
# Divide
def divide(n1, n2):
  return n1/n2

def calculator():
  print(logo)

  num1 = float(input("What's the first number? : "))
  
  should_continue = True
  while should_continue:
    for operation in operations:
      print(operation)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? : "))
  
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_operation = input(f"Type 'y' to continue calculating with {answer}  or type 'n' to exit.: ").lower()
    
    if continue_operation == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

calculator()