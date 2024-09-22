class Atm:
  def __init__(self):
    self.__pin = ''   # Interpreter converts it to: __Atm__pin
    self.__balance = 0  # Interpreter converts it to: __Atm__balance
    print(id(self))
    self.__menu()

  def get_pin(self):
    return self.__pin
  def set_pin(self,new_pin):
    if type(new_pin) == 'str':
      self.pin = new_pin
      print('Pin changed')
    else:
      print('Not Allowed')

  def __menu(self):
    user_input = input("""
          Hello! How would you like to proceed?
          1. Create Pin
          2. Deposit
          3. Withdraw
          4. Check balance
          5. Exit
    """)
    if(user_input == '1'):
      self.create_pin()
      self.__menu()
    elif(user_input == '2'):
      self.deposit()
      self.__menu()
    elif(user_input == '3'):
      self.withdraw()
      self.__menu()
    elif(user_input == '4'):
      self.check_balance()
      self.__menu()
    elif(user_input == '5'):
      self.exit_atm()
  
  def create_pin(self):
    self.__pin = input('Enter your new pin: ')
    print('Pin set sucessfully')

  def deposit(self):
    tempPin = input('Enter your pin: ')
    if tempPin == self.__pin:
      amount = int(input('Enter amount to deposit: '))
      self.__balance = self.__balance + amount
      print('Deposited successfully')
    else:
      print('Invalid Pin. Try again!!')
      self.deposit()

  def withdraw(self):
    tempPin = input('Enter your pin: ')
    if tempPin == self.__pin:
      amount = int(input('Enter amount to withdraw: '))
      if amount < self.__balance:
        self.__balance = self.__balance - amount
        print('Withdraw successful')
      else:
        print('Insufficient funds')
    else:
      print('Invalid Pin. Try again!!')
      self.withdraw()

  def check_balance(self):
    tempPin = input('Enter you pin: ')
    if tempPin == self.__pin:
      print('Your current balance is:' + str(self.__balance))
    else:
      print('Invalid Pin. Try again!!')
      self.check_balance()

  def exit_atm(self):
    print('Thank you for using our ATM service')

sbi = Atm()


# Implementation of Encapsulation:
# Data members and methods are prefixed by __ which made them private and they cannot be accesses outside the class scope
# sbi.balance creates a new instance
# After prefixing instances by __ , the instance is replaced by _ClassName__InstanceName.
# Initially, sbi.pin, sbi.__pin, sbi.balance, sbi.__balance cannot be accessed because they are not created. After creation(assigning values to them), they can be accessed. They are created separately and doesnt affect the program since they are not used anywhere.
# The instance variable of the class can be accessed and modified by sbi._Atm__balance
# Nothing in Python is TRULY PRIVATE