Source: https://www.youtube.com/playlist?list=PLd3UqWTnYXOnpAvWhPcnxyfGDyXf-2WVW

Class
Object 
Reference Variable

Class: Blue print
Object: The physical representation of the class
Reference Variable- To refer object and invoke the required functionality 


EG:
Class: TV Blue Print of a specific Model
Object: The Physical TV that can be produced out of it. (we can have many objects for a single class.)
Reference Variable: The Remote with which we control the TV (we can have many reference variable for single object.)

An object will have properties and behaviour

Properties(Data) are specified by variables
behaviour can be specified by methods

Types of Variables:

    1. Instance Variables (object level)
    2. Static Variables (Class level)
    3. Local Variables (Method level)

Types of Methods:

    1. Instance Method (object related methods are called instance method)
    2. Class Method
    3. Static Method

To create an reference variable. 

"<reference_variable_name> =<classname>"
# _______________________________________________________________________________________________________________________________________________

Explanation of self in a class:

    1. self is a reference variable, which is always pointing to the current object within python class, to access the current object we can use self.
    2. The first argument to the constructor is always self
    3. The first argument to the instance method is always self. We need not provide value for self variable the Python virtural machine will provide the value. 
    4. We can use self always within the class only.
    5. Inside the constructor, we can use self to declare the object related variables (instance Variables.)
    6. Inside instance method, we can use self to access the value of instance variables. 
    7. 

# _______________________________________________________________________________________________________________________________________________

Explanation of constructor in a class:

    1. Constructor is a special method
    2. it is always named as __init__ (this means initialize)
    3. we need not call the constructor explicitly. 
    4. It will be executed automatically when we create the object. 
    5. per object it will be executed only once and we can have many object for a class. 
    6. The main purpose of the Constructor is to declare and initialize the instance variable. 
    7. Constructor should take atleast 1 argument which is self. 
    8. within python class constructor is optional if we dont provide prython virtual machine will provide the constructor default value. 
    9. We can call constructor explicitly like a normal method. and new object wont be created. 
    10. Overloading constructor and method is not applicable. PVM will take the last constructor into account and delete the old constructor. 

# _______________________________________________________________________________________________________________________________________________

Types of Variables and Types of Methods

Basic Ideas of Variables:
    1. Instance Variables (Name RollNo....)- Object Level Variables:

        If the value of the variable changes from object to object (Name Roll Number... ) it is called instance variable. 
        For every object a seperate copy is created. 
        In general we can define the instance vairable inside constructor (__init__) using self. 
        We can also define default value for the instance variable inside __init__

    2. Static Variables/ Class level Variables:  
        If the value of the variable does not change object to object (eg. College name...) then it is not recommened to be declared that variable as instance variable as it will create different copy every time.
        In the case of instance variable for every object we create a spearate copy. But in case of static variables. A singe copy will be created and shared to every object of the class.
        Most of the times, static variables shoudl be declared within the class directly.
    3. Local Variables - Method level Variables:
        To meet the temporary requirements of the programmer, we can declare the variable directly inside the method. 
# ___________________________________________________________________________________________________________________


Basic Ideas of Methods:
    1. Instance Method:

        If we are accessing instance variable then it is the instance method. Irrespective of using static and local variable.
        The first argument to the instance method is "self" which is pointing to the current object
        decorator is not needed

    2. Class Method:
        If we are not using any instance variable, but we are using the static variable (Class variable) then this is class method. 
        the first argument to the class method is "cls" which is pointing to the corresponding class variable. 
        decorator is @classmethod

    3. Static Method
        If we are not using any instance variable as well as the static variables then this method has no way related to this object and class then it is the general utility method we have to declate this as static method. 
        No variable is needed. 
        decorator is @staticmethod. 
# ___________________________________________________________________________________________________________________

Places to declare instance variable. 
    1. Inside the constructor using self (__init__)
    2. Inside instance method by using self 
    3. Outside of the class by using object reference. 

How to access instance variable.
    1. Within the class using self. 
    2. Outside the class with the object name reference. 

How to update the instance variable. 
    While calling the object you can give the variable name and update outside the class. 
    eg: t1.a=999

How to delete the instance variable.
    Within the class:
        del self.variable name
    Outside the class
        del objectreference.variablename. 

# ___________________________________________________________________________________________________________________


Story of Static Variable:
    If the value of the variables are not varied from object to object. 
    Only one copy of this variable created for the all the objects. 
    It can be created within the class in general. 

Various Place to Declare:
    1. We can declare any place. 
    But in general we declare it within the class outside any method directly. 
    2. Inside the constructor and instance method using class name. 
    3. Inside class method using either class name or cls variable
    4. Inside static method using the class name. 
    5. Outside the class, by using class name. 
    However these 4 conditions that are outside the constructor, each method should be explicitly called. 

How to access the Static Variable:
    We can access the static variable inside a method using self or class name or cls, or object reference. 

How to modify the Static Variables:
    We should update the value of static variable either by classname or cls variable. we cannot use self or object reference to update the static variable. 


How to delete the Static Variable. 
    Anywhere:
        del classname.variable name
    Inside the classmethod:
        del cls.variablename. 
    we cannot update or delete static variable by using self or object reference. 


# ___________________________________________________________________________________________________________________


Local Variables/ Method level variable or temporary variable. 

How to declare Local Variable:
    We can declare local variable directly inside the method The validity is inside the method only. 