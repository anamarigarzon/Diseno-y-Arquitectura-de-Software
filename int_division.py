class Integer_Division(Operation):
  def __init__(self,num1,num2, op ='//'):
    super().__init__(num1, num2, op)
    self.op = op
    if num2 == 0:
      self.result = "Divisor no válido"
    else:
      self.result = int(num1 / num2)
