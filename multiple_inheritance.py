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


z=Stud()
z.name()
z.num()
z.std()

# <---Same name functions on the Parent_Class and Child_Class--->
class Office:
    def name(self):      #<...Same Name Of Child_Class...>
        print("Bridgeon")

class Batch:             
    def num(self):
        print(3)

class Stud(Office,Batch):
    def name(self):     #<...Same Name of Parent_Class...>
                        # <---If giving here the same name function of Parent_class. will get the Child_Class objects not Parent---> 
        print("Anshad")


z=Stud()
z.name()
z.num()
z.name()



# <---Same Name fuctions for Two Parent_class--->
class Office:
    def name(self):
        print("Bridgeon")

class Batch:            # <---If giving here the same name function for Two Parent_Class. Will get the first Parent_Class objects---> 
    def name(self):
        print(3)

class Stud(Office,Batch):
    def std(self):       
        print("Anshad")


z=Stud()
z.name()
z.name()
z.std()

