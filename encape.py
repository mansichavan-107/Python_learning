# public variable
# create a student classs with a public variable name and dispay the name
"""class student:
    def __init__(self):
        self.name = "mansi"

s1 = student() 
print(s1.name)"""

#private variable
#reate a employee class with a private variable salary. access it using a getter method
"""class Employee:
    def __init__(self):
        self.__salary = 25000

    def get_salary(self):
        return self.__salary

e1 = Employee() 
print (e1.get_salary()) """  

# getter and setter
# create a  student class.set and get the student name using getter and setter methods
"""class student:
    def __init__(self):
        self.__name = "mansi"

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

s1 = student()
print(s1.get_name())
s1.set_name("priya")
print(s1.get_name())"""

# private variable with age
# create a person class with a private age variable. dispay age using getter.
"""class Person:
    def __init__(self):
        self.__age = 20

    def get_age(Self):
        return Self.__age

p1 = Person()
print(p1.get_age())  """

# setter with validation
# create an employee class.set salary only greter than zero.
"""class Employee:
    def __init__(self):
      self.__salary = 0

    def set_salary(self,salary):
       if salary > 0:
          self .__salary = salary
       else:
          print("invalid salary")

    def get_salary(self):
       return self .__salary
    
e1 = Employee()

e1.set_salary(30000)
print(e1.get_salary())

e1.set_salary(-500)"""
            
# public and private variables
# create a bank class with a public bank name and private name.
"""class Bank:
    def __init__(self):
        self.bank_name = "SBI"
        self.__balance = 5000

    def get_balance(self):
        return self.__balance

b1 = Bank()
print (b1.bank_name)
print (b1.get_balance()) """         

# protected variable.
# create a parent class with a protected variable and access it from a child class
"""class Parent:
    def __init__(self):
        self ._name ="mansi"

class child (Parent):
    def display (self):
        print (self._name)

c1 = child()
c1.display()"""   

# private variable with multiplication
# create a calculator class with two private variables.display their multiplication using a methood
"""class Calculator:
    def __init__(self):
        self.__a = 10
        self.__b = 5

    def multiply(self):
        return self.__a * self.__b
        
c1 = Calculator()
print(c1.multiply())"""

# getter and setter for marks
# create a student class with private marks.use gretter and setter to update marks.
"""class Student:
    def __init__(self):
        self.__marks = 80

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid marks")

s1 = Student()
print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())"""

# bank account deposit and withdraw
# create a bank account class with a private balance.create deposit,withdraw and display methods.
"""class BankAccount:
    def __init__(self):
        self .__balance = 10000

    def deposit(self,amount):
        if amount > 0:
            self .__balance += amount
            print("amount deposited")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("amount withdrawn")
        else:
            print("insufficient balance or invalid amount")

    def display(self):
        print("balance:",self.__balance)


b1 = BankAccount()

b1.deposit(2000)
b1.withdraw(1000)
b1.display()"""

# create a product class with a private variable price.display the price using a getter method.
"""class product:
    def __init__(self):
        self.__price = 1500

    def get_price(self):
        return self.__price

p1 =  product()
print("price:",p1.get_price())"""   

# create a mobile class with a private variable brand.set the brand to samsung and display it.
"""class Mobile:
    def __init__(self):
        self.__brand =""

    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

m1 = Mobile()
m1.set_brand("samsung")

print(m1.get_brand())"""

# create a student class.set marks and checks wheter the student passed or failed.passing marks are 35.
"""class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,marks):
        self.__marks = marks

    def get_result(self):
        if self.__marks >= 35:
            print("pass")
        else:
            print("fail")

s1 = Student()
s1.set_marks(75)
s1.get_result()"""

# craete a class with public employee name and private employee id.display both.
"""class Employee:
    def __init__(self):
        self.name = "rahul"
        self.__emp_id = 101
    
    def get_id(self):
        return self .__emp_id

e1 = Employee()

print("name:",e1.name)
print("id",e1.get_id())""" 

# create a private balnce variable. add money using a deposit method and display the updated balance.
class Bank:
    def __init__(self):
        self.__balance = 5000

    def deposit(self,amount):
        if amount >0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

b1 = Bank()
b1.deposit(2000)

print("balance:",b1.get_balance())










                  
