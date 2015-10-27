class myIterableObject:
  def __init__(self, minValue, maxValue):
    self.current = minValue
    self.maximum = maxValue
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.maximum:
      raise StopIteration
    else:
      self.current = self.current + 1
      return self.current - 1


for i in myIterableObject(1,10):
  print(i)