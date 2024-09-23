class Coordinate:
  def __init__(self,x=0,y=0):
    self.x_cord = int(x)
    self.y_cord = int(y)
  
  def __str__(self):
    return '({},{})'.format(self.x_cord,self.y_cord)  
  
  def __add__(self,other):
    temp = Coordinate()
    temp.x_cord = self.x_cord + other.x_cord
    temp.y_cord = self.y_cord + other.y_cord
    return temp

  def __sub__(self,other):
    temp = Coordinate()
    temp.x_cord = self.x_cord - other.x_cord
    temp.y_cord = self.y_cord - other.y_cord
    return temp  
  
  def calculate_slope(self,other):
    if self.x_cord == other.x_cord:
      return 'Line is parallel to y-axis'
    else:
      return ((other.y_cord-self.y_cord)/(other.x_cord-self.x_cord))
    
  def line_equation(self,other):
    if other.x_cord-self.x_cord > 0:
      return f'{other.y_cord - self.y_cord}x - {other.x_cord-self.x_cord}y = {self.x_cord*other.y_cord - other.x_cord*self.y_cord}'
    else:
      return f'{other.y_cord - self.y_cord}x + {-(other.x_cord-self.x_cord)}y = {self.x_cord*other.y_cord - other.x_cord*self.y_cord}'

  def distance(self,other):
    return ((other.x_cord-self.x_cord)**2 + (other.y_cord-self.y_cord)**2 )**(1/2)


print('Enter first coordinate:')
c1 = Coordinate(input('Enter x-coordinate: '),input('Enter y-coordinate: '))
print('Enter second coordinate:')
c2 = Coordinate(input('Enter x-coordinate: '),input('Enter y-coordinate: '))

c3 = c1+c2
print(f'The sum is: {c3}')

c4 = c1-c2
print(f'The difference is: {c4}')

slope = c1.calculate_slope(c2)
print(f'The slope is: {slope}')

print('Equation of line is:', c1.line_equation(c2))

print('Distance between points: ', (c1.distance(c2)))