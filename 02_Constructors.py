class Airplane:
  def __init__(self):       # default constructor
    print('Default constructor called')
  def AirplaneMethod1(self):
    print('Method 1 called')
  def AirplaneMethod2(self):
    print('Method 2 called')
my_airplane = Airplane()
my_airplane.AirplaneMethod1()
my_airplane.AirplaneMethod2()


class Car:
  def __init__(self,brand,model,year):    # parameterized constructor
    self.brand = brand
    self.model = model
    self.year = year
  def showData(self):
    print('Brand:' + self.brand)
    print('Model:' + self.model)
    print('Year:' + str(self.year))

my_car = Car('Tesla','Model S',2022)
my_car.showData()


class Bus:
  def __init__(self,brand1,model1,year1):    # parameterized constructor
    self.brand = brand1     #data members of the class
    self.model = model1
    self.year = year1
  def showData(self):
    print('Brand:' + self.brand)
    print('Model:' + self.model)
    print('Year:' + str(self.year))

my_bus = Bus('Scorpio','Model 5',2025)
my_bus.showData()
