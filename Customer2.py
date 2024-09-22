#collection of objects
class Customer:
  def __init__ (self,name,age):
    self.name = name
    self.age = age
  
  def intro(self):
    print('I am',self.name,'and my age is',self.age)
  
c1 = Customer('Hari',56)
c2 = Customer('Shyam',23)
c3 = Customer('Gita',86)

L1 = [c1,c2,c3]

# for i in L1:
#   print('Using for loop: ')
#   print(i.name, i.age)

for i in L1:
  i.intro()


