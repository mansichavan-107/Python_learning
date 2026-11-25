# single inheritance
# create a parent class animal with a method eat(). create a child dogg with a method bark().display both methods.
"""class Animal:
    def eat(self):
        print("animal is eating")

class dog(Animal):
    def bark(self):
        print("dog is barking")

d1 = dog()
d1.eat()
d1.bark()"""

# create a student parent class with name and a child class result with marks.display both
"""class student:
    def show_name(self):
        print("name:mansi")

class result(student):
    def show_marks(self):
        print("marks : 85")        
            

r1 = result()
r1.show_name()
r1.show_marks() """

# create a vehicle class with start and a car class with drive().
"""class Vehicle:
    def start (self):
        print("vehicle started")

class Car(Vehicle):
        def drive(self):
            print("Car is driving")

c1=Car()
c1.start()
c1.drive()"""

# create an employee class with slary and a manager class with bonus.display total salary
"""class employee:
    def salary(self):
        return 25000

class manager(employee):
    def bonus(self):
        return 5000

m1 =  manager()

total = m1.salary()+m1.bonus()
print("total salary:",total)"""

# create a calculator parent class with addition and a child class with multiplication
"""class calculator:
    def add(self,a,b):
        print("addition:",a+b)

class advancecalculator(calculator):
    def multiply(self,a,b):
        print("multiplication:",a*b)

c1 = advancecalculator()
c1.add(10,20)
c1.multiply(10,20) """

# create three classes  and display messages from all three classe.
"""class grandfather:
    def show1(self):
        print("i am grandfather")

class father(grandfather):
    def show2(self):
        print("i am father")

class son(father):
    def show3(self):
        print("i am son") 

s1=son()
s1.show1()
s1.show2()
s1.show3()"""

# multilevel inheritance
# create a person,student and exam classes.display name,course and marks
"""class person:
    def name(self):
        print("name:mansi")

class student(person):
    def course(self):
        print("course:python")

class exam(student):
    def marks(self):
        print("marks:90")

e1 = exam()
e1.name()
e1.marks()
e1.course()"""

# create three classes using multilevel inheritance and display company,department and employee details.
"""class company:
    def company(self):
        print("company:infosys")

class department(company):
    def departmnet(self):
        print("departmnet:IT")

class employee(department):
    def employee(self):
        print("employee:rahul")

e1 = employee()
e1.company()
e1.departmnet()
e1.employee()"""

# create three classes.display their respective characteristics
"""class animal:
    def eat(Self):
        print("animal eat food")

class mammal(animal):
    def walk(self):
        print("mammals can walk")

class human(mammal):
    def think(self):
        print("humans can think")

h1 = human()
h1.eat()
h1.think()
h1.walk()"""

# create a  shape class,rectangle child class and square child using multilevel inheritance.calculate square area.
"""class shape:
    def display(self):
        print("this is a shape")

class rectangle(shape):
    def info(self):
        print("rectangle and square")

class square(rectangle):
    def area(self,side):
        print("area:",side*side)

s1 = square()
s1.display()
s1.info
s1.area(5) """

# multiple inheritance
# create two parent classes father and mother.access both methods using child class.
"""class father:
    def skills1(self):
        print("father:....driving")

class mother:
    def skills2(self):
        print("mother:....cooking")

class child(father,mother):
    def skills3(self):
        print("child:.....learning python")

c1 = child()
c1.skills1()
c1.skills2()
c1.skills3()"""

# create two parent classes for addition and substraction.create a child class for both
"""class addition:
    def add(self,a,b):
        print("addition:",a+b)

class subtraction:  
    def sub(self,a,b):
        print("substraction:,a-b")

class calculator(subtraction):
    pass

c1 = calculator()
c1.add(20,10)
c1.sub(20,10)"""

# create two parent classes camera and music player. access both methods in mobile.
"""class camera:
    def photo(self):
        print("taking photo")

class musicplayer:
    def music(self):
        print("playing music")

class mobile(camera,musicplayer):
    def call(self):
        print("calling")

m1 = mobile()
m1.photo()
m1.music()
m1.call()  """

# create teacher and researcher parent classes.create professor child class.
"""class teacher:
    def teach(self):
        print("teaching students")

class researcher:
    def reserch(self):
        print("doing research")

class professor (teacher,researcher):
    def display(self):
        print("i am professor")

p1 = professor()
p1.teach()
p1.reserch()
p1.display()"""

# hierarchical inheritance
# create one parent class animal and two child classes dog and cat.
"""class animal:
    def eat(self):
        print("eating dog")

class dog(animal):
    def bark(self):
        print("dog barking")

class cat(animal):
    def sound(self):
        print("cat meowing")

d1 = dog()                         
d1.eat()
d1.bark()

c1 = cat()
c1.eat()
c1.sound()"""

# create a bank parent class and savings and current child classse.
class bank:
    def bank_name(self):
        print("bank:...sbi")

class saving(bank):
    def account(self):
        print("saving account")

class current(bank):
    def account(self):
        print("current account")

s1 = saving()
s1.bank_name()
s1.account()

c1 = current()
c1.bank_name()
c1.account()






        
    

        
    


 

    


