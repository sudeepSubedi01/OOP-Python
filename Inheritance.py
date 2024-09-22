class User:
  def login(self):
    print("Logged in")
  def register(self):
    print('Registered')

class Student(User):
  def enroll(self):
    print('Enroll')
  def review(self):
    print('Review')

s1 = Student()
s1.login()
s1.register()
s1.enroll()
s1.review()
