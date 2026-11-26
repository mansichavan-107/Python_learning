# 1) animal
"""from abc import ABC , abstractclassmethod

class animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("dog barks")

class cat(animal):
    def sound(self):
        print("cat meows")

d = dog()
d.sound()

c = cat()
c.sound()"""

# 2) vehicle
"""from abc import ABC,abstractclassmethod
class vehicle(ABC):
    @abstractclassmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("car start with a key")

c = car()
c.start() """

# 3) bank
"""from abc import ABC , abstractclassmethod
class bank(ABC):
    @abstractclassmethod
    def interest(self):
        pass

class sbi(bank):
    def interest(self):
        print("sbi interest is 7%")

class hdfc(bank):
    def interest(self):
        print("hdfc interest is 8%")

s = sbi()
s.interest()

h = hdfc()
h.interest()"""

# 4) payment
"""from abc import ABC,abstractclassmethod
class payment(ABC):
    @abstractclassmethod
    def pay(self,amount):
        pass

class googlepay(payment):
    def pay(self, amount):
        print("paid",amount,"using google pay")

p =googlepay()
p.pay(500) """

# 5) mobile
"""from abc import ABC,abstractclassmethod
class mobile(ABC):
    @abstractclassmethod
    def call(self):
        pass

class android(mobile):
    def call(self):
        print("calling from android")

m = android()
m.call()   """

# 6)employee
"""from abc import ABC,abstractclassmethod
class employee(ABC):
    @abstractclassmethod
    def salary(self):
        pass

class manger(employee):
    def salary(self):
        print("manager salary is 50000")

e = manger()
e.salary()  """  

# 7) shape
"""from abc import ABC,abstractclassmethod
class shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class rectangle(shape):
    def area(self):
        print("area = 10",10*20)

r = rectangle()
r.area() """

# 8)laptop
"""from abc import ABC,abstractclassmethod
class laptop(ABC):
    @abstractclassmethod
    def process(self):
        pass

class dell(laptop):
    def process(self):
        print("dell laptop is processing")

l = dell()
l.process()  """

# 9) food
"""from abc import ABC,abstractclassmethod
class food(ABC):
    @abstractclassmethod
    def prepare(self):
        pass

class pizza(food):
    def prepare(self):
        print("pizza is very testy")

class burger(food):
    def prepare(self):
        print("preparing burger")

p = pizza()
p.prepare()
b =burger()
b.prepare() """

# 10)school
"""from abc import ABC,abstractclassmethod
class school(ABC):
    @abstractclassmethod
    def exam(self):
        pass

class student(school):
    def exam(self):
        print("students gives exam")

s = student()
s.exam() """

# 11) calculator
"""from abc import ABC,abstractclassmethod
class calculator(ABC):
    @abstractclassmethod
    def calculate(self,a,b):
        pass

class addition(calculator):
    def calculate(self, a, b):
        print("addition =",a+b)

c = addition()
c.calculate(10,20)"""

# 12)hospital
"""from abc import ABC,abstractclassmethod
class hospital(ABC):
    @abstractclassmethod
    def treatement(self):
        pass

class doctor(hospital):
    def treatement(self):
        print("doctor provides treatment")

d = doctor()
d.treatement()"""

# 13) printer
"""from abc import ABC,abstractclassmethod
class printer(ABC):
    @abstractclassmethod
    def print_document(self):
        pass

class hp(printer):
    def print_document(self):
        print("printing document using hp")

p = hp()
p.print_document()"""

# 14) electricity
"""from  abc import ABC,abstractclassmethod
class electricity(ABC):
    @abstractclassmethod
    def supply(self):
        pass

class home(electricity):
    def supply(self):
        print("electricity supplied to home")

h = home()
h.supply()"""   

# 15) delivery
"""from abc import ABC,abstractclassmethod
class delivery(ABC):
    @abstractclassmethod
    def deliver(self):
        pass

class amazon(delivery):
    def deliver(self):
        print("amazon delivers the product")

a = amazon()
a.deliver()  """

# 16)bank account
"""from abc import ABC,abstractclassmethod
class accounnt(ABC):
    @abstractclassmethod
    def withdraw(self,amount):
        pass

class saving_account(accounnt):
    def withdraw(self, amount):
        print("withdraw amount:",amount)

s = saving_account()
s.withdraw(500) """

# web browser
"""from abc import ABC,abstractclassmethod
class browser(ABC):
    @abstractclassmethod
    def open_website(self):
        pass

class chrome(browser):
    def open_website(self):
        print("opening website in chrome")

c = chrome()
c.open_website() """

# transport
"""from abc import ABC,abstractclassmethod
class transport(ABC):
    @abstractclassmethod
    def travel(self):
        pass

class bus(transport):
    def travel(self):
        print("traveeling by bus")

class train(transport):
    def travel(self):
        print("travelling by bus")

b =  bus()
b.travel()

t=train()
t.travel()"""

# 19) course
"""from abc import ABC, abstractclassmethod
class course(ABC):
    @abstractclassmethod
    def study(self):
        pass

class python(course):
    def study(self):
        print("learning python")

p =python()
p.study()"""

# 20) online shopping
from abc import ABC,abstractclassmethod
class shopping(ABC):
    @abstractclassmethod
    def order(self):
        pass

class amazon(shopping):
    def order(self):
        print("order placed by successfully")

class flipkart(shopping):
    def order(self):
        print("order placed on flipkart")

a = amazon()
a.order()

f = flipkart()
f.order()




        