class MyClass:
    cls=10
    def __new__(cls):
        # Create a new instance of MyClass
        instance = super(MyClass, cls).__new__(cls)
        # Additional customizations here
        return instance

obj = MyClass()  # Calls __new__ and then __init__
print(obj.cls)


class MyClass:
    
    # def __new__(cls):
    #     # Create a new instance of MyClass
    #     instance = super(MyClass, cls).__new__(cls)
    #     return instance

    def __init__(self):
        self.my_variable = 20  # Set the variable value during initialization

obj = MyClass()  # Calls __new__ and then __init__
print(obj.my_variable)  # Print the variable value