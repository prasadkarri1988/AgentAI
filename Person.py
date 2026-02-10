class Person:
  def __init__(self, name,age):
    self.name = name
    self.age=age

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  def setName(self,name):
    self.name=name

  def setAge(self,age):
      self.age=age

p1 = Person("prasad",38)
print(p1.getName())
print(p1.getAge())

