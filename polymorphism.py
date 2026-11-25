# method overloading
"""class calculator:

    def add(self,a,b=0,c=0):
        print("addition:",a+b+c)

obj = calculator()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)"""

# method overriding
"""class parent:
    def show(self):
        print("parent class")

class child(parent):
    def show(self):
        print("child class")

obj = child()
obj.show() """

# animal sound
"""class animal:
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")

obj = dog()
obj.sound()"""

"""class vehicle:
    def start(self):
        print("vehicle starts")

class car(vehicle): 
    def start(self):
        print("car starts with key")

obj = car()
obj.start()"""

# student
"""class student:
    def dispay(self):
        print("student details")

class college(student):
    def dispay(self):
        print("college student details")

obj = college()
obj.dispay() """

# bank
"""class bank:
    def interest(self):
        print("bank interest")

class sbi(bank):
    def interest(self):
        print("sbi interest rate is 7%")

obj = sbi()
obj.interest()"""

"""class employee:
    def salary(self):
        print("employee salary")

class manager(employee):
    def salary(self):
        print("manager salary is 5000")

obj = manager()
obj.salary() """

# mobile
"""class mobile:
    def camera(self):
        print("mobile has camera")

class samsung(mobile):
    def camera(self):
        print("samsung has 50mp camera")

obj = samsung()
obj.camera()"""

#shape 
"""class shape:
    def area(self):
        print("area of shape")

class rectangle(shape):
    def area(self):
        print("area = length * width")

obj = rectangle()
obj.area() """

# person
"""class person:
    def work(self):
        print("person is working")

class teacher:
    def work(self):
        print("teacher is teaching")

obj = teacher()
obj.work()  """      

# payment
"""class payment:
    def pay(self):
        print("payment process")

class upi(payment):
    def pay(self):
        print("payment using upi")

obj = upi()
obj.pay()"""

# food 
"""class food:
    def taste(Self):
        print("food has taste")

class pizza(food):
    def taste(Self):
        print("pizza is testy")

obj = pizza()
obj.taste() """

#laptop
"""class laptop:
    def display(self):
        print("laptop display")

class lenovo(laptop):
    def display(self):
        print("lenovo laptop display")

obj = lenovo()
obj.display()"""

#animal eating
"""class animal:
    def eat(self):
        print("animal eats food")

class cow(animal):
    def eat(self):
        print("cow eat grass")

obj = cow()
obj.eat()"""

# calculator
class calculator:
    def calculator(self):
        print("basic calculation")

class advancedcalculator(calculator):
    def calculator(self):
        print("advanced calculation")

obj = advancedcalculator()
obj.calculator()                
            
                






