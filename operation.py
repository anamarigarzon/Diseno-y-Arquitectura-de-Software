from abc import abstractmethod
class Operation:
  def __init__(self, num1, num2, op):
    self.num1 = num1
    self.num2 = num2
    self.op = op

  @abstractmethod
  def operate(self):
    print(f'{self.num1} '+ self.op + f' {self.num2} = ' + str(self.result))
