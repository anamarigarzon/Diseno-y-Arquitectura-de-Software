from operation import Operation

class CalculatorFacade:
  def __init__(self):
    pass
  def execute_binary_operation(self,num1,num2, binary_operation):
    if binary_operation == "+":
      op = Addition(num1,num2)
    elif binary_operation == "-":
      op = Subtraction(num1,num2)
    elif binary_operation == "*":
      op = Multiplication(num1,num2)
    elif binary_operation == "/":
      op = Division(num1,num2)
    elif binary_operation == "//":
      op = Integer_Division(num1,num2)
    elif binary_operation == "^":
      op = Potentiation(num1,num2)
    elif binary_operation == "%":
      op = Module(num1,num2)
    else:
      print("non-recognizable operation")
  def execute_unary_operation(self, unary_operation): ## Aún no está definido
    pass
