class Coordinate:
  # def __init__(self,x,y):
  #   self.x_cord = x
  #   self.y_cord = y
  
  def __add__(self,other):
    temp = Coordinate(0,0)
    temp.x_cord = self.x_cord + other.x_cord
    temp.y_cord = self.y_cord + other.y_cord
    return temp

  def get_coordinates(self):
    self.x_cord = input('Enter x-coordinate: ')
    self.y_cord = input('Enter y-coordinate: ')
  
  def show_coordinates(self):
    print('(x,y) =','(',self.x_cord,',',self.y_cord,')')

c1 = Coordinate()
c2 = Coordinate()

c1.get_coordinates()
c2.get_coordinates()

c1.show_coordinates()
c2.show_coordinates()