                    #_____Constructors______#

class Office:
    name="Mufees"

    print("Defualt Constructor")

    def intern(self):
        print(self.name)

z=Office()
z.intern()



class Staff:
    def __init__(self,name):
        self.name=name

        print("Parameterized")

    def display(self):
        print(self.name)

x=Staff("Shahin")
x.display()


class Student:
    def __init__(self):
        print("None-Parameterized")

    def std(self,name):
        print(name)

y=Student()
y.std("Salman")



                #_____Inheritance_____#

            # <-----Single Inheritance----->

class Office:
    def batch(self):
        print(7)

class Intern(Office):
    def student(self):
        print("Ameer")

x=Intern()
x.batch()
x.student()



                # <---Multi-level Inheritance--->

class Domain:
    def web(self):
        print("Python")

class Student(Domain):
    def name(self):
        print("Safvan")

class Week(Student):
    def week(self):
        print(8)

y=Week()
y.name()
y.web()
y.week()

                    # <---Multiple Inheritance--->
class Office:
    def name(self):
        print("Bridgeon")

class Batch:            # <---If giving here the same name function for Two Parent_Class. Will get the first Parent_Class objects---> 
    def num(self):
        print(3)

class Stud(Office,Batch):
    def std(self):       # <---If giving here the same name function of Parent_class. will get the Child_Class objects not Parent---> 
        print("Anshad")

                        #(___All code in multiple_inheritance.py file___)
z=Stud()
z.name()
z.num()
z.std()



                        # <---Hierarchical inheritance--->

class Vehicle:
    def category(self):
        print("Four Wheel")

class Jeep(Vehicle):
    def thar(self):
        print("Black Thar")
j=Jeep()
j.thar()
j.category()

class Toyota(Vehicle):
    def baleno(self):
        print("Navey Blue")
t=Toyota()
t.baleno()
t.category()

class Benz(Vehicle):
    def sclass(self):
        print("White S-Class")

b=Benz()
b.sclass()
b.category()



                    # <---Scops-Global and Local--->


global_v = "Salman"

def any_func():
    local_v = "Anshad"
    print(local_v)
    print(global_v)
any_func()

def some_func():
    print(global_v)
    # print(local_v) "It is can't access. Becouse it is Local Variable"
some_func()



                            # <---Super Keyword--->

class Office:
    def __init__(self,course):
        self.course=course

    def std(self):
        print(f"Course is {self.course}")


class Domain(Office):
    def __init__(self,name,course):
       super().__init__(course)
       self.name=name

    def stud(self):
        print(f"Domain is {self.name}")

y=Domain("Python","Web Development")
y.std()
y.stud()


                # <---Abstraction--->

from abc import ABC , abstractmethod

class Myname(ABC):
    def me(self):
        pass

class Iam(Myname):
    def __init__(self,name):
        self.name=name

    def me(self):
        return self.name

x=Iam("Salman")
print(x.me())



