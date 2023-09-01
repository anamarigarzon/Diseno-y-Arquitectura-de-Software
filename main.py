from calculator_facade import CalculatorFacade

calculator = CalculatorFacade() # Create calculator instance

num1 = 20
num2 = 5
num3 = 0

print("Addition")
calculator.execute_binary_operation(num1,num2,'+')

print("/n Subtraction")
calculator.execute_binary_operation(num1,num2,'-')

print("/n Multiplication")
calculator.execute_binary_operation(num1,num2,'-')

print("/n Division")
calculator.execute_binary_operation(num1,num2,'/')
calculator.execute_binary_operation(num1,num3,'/')

print("/n Integer Division")
calculator.execute_binary_operation(num1,num2,'//')
calculator.execute_binary_operation(num1,num3,'//')

print("/n Potentiation")
calculator.execute_binary_operation(num1,num2,'^')

print("/n Module")
calculator.execute_binary_operation(num1,num2,'%')
calculator.execute_binary_operation(num1,num3,'%')
