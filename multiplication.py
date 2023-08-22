class Multiplication(Operation):
  def __init__(self,num1,num2, op='*'):
    super().__init__(num1, num2,op)
    self.op = op
    self.result = num1 * num2
