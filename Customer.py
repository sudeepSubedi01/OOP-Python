# pass by reference and returning object
class Customer:
  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

def greet(c2):
  if c2.gender == 'male':
    print('Hello',c2.name, 'sir')
  else:
    print('Hello',c2.name,'miss')
  c3 = Customer('Sita','female')
  return c3

c1 = Customer('HariLal','male')
# print(cust.name)
c3 = greet(c1)
print(c3.name)