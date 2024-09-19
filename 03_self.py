class Student:
  def __init__(self):
    self.name = 'n/a'
    self.roll = 0
  
  def getData(self):
    self.name = input("Enter your name:")
    self.roll = int(input("Enter your roll:"))
  
  def showData(self):
    print('Name = ' + self.name)
    print('Roll = ' + str(self.roll))
    print('id(self) = '+ str(id(self)))

s1 = Student()
s1.showData()
s1.getData()
s1.showData()
print('id(s1) = ' + str(id(s1)))



# both s1 and self are stored in the same memory address
