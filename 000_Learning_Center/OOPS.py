
#_______________________________________________________________________________________________________________________________________________

class Student:
    """This class is for demo purpose only and this doc string is optional can be accessed by __doc__ attribute or by help() function"""

    "The class name is Student and it has Two methods __init__ and talk."

    # Variables (properties) like name, marks, rollno....
    # Methods (functions) like read, write, sleep, eat, talk....

    def __init__(self,name,marks,rollno): # This is constructor which is used to initialize the object of the class
        # print("Constructor Executed...")
        self.name = name
        self.marks = marks
        self.rollno = rollno
    def talk(self):
        print("Hello, I am: ",self.name)
        print("My marks are: ",self.marks)
        print("My roll number is: ",self.rollno)


#print(Student.__doc__)
# help(Student)


#Creating the object of the class

s1 = Student("Vikram",95,11209189) # s1 is the reference variable. 
s2 = Student("Pallavi",100,1223012)
s1.talk()
s2.talk()
# s2 = Student()
# print(id(s1))
# print(id(s2))
# print(s.name)
# print(s.rollno)
# print(s.marks)
# s.talk()
print("Student1", s1.name, s1.marks, s1.rollno)
print("Student2", s2.name, s2.marks, s2.rollno)

#_______________________________________________________________________________________________________________________________________________
class Test:
    def __init__(self):
        print("address of object refered by self is :", id(self))

t1 = Test()
print("address of object refered by t1 is :", id(t1))
t2 = Test()
print("address of object refered by t2 is :", id(t2))


#_______________________________________________________________________________________________________________________________________________

class Test1:
    def __init__(self):
        print("no-arg construtor")
    def __init__(self,x):
        print("arg construtor",x)


t=Test1(10)

class Test2:
    def Testing(self):
        print ("A Special method")

t=Test2() # __init__() will be executed
t.Testing() # method will be executed

#_______________________________________________________________________________________________________________________________________________

class Employee:
    def __init__(self, name,age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def get_bonus(self):
        bonus=self.salary*.05
        return bonus
    

e1=Employee("Vikram", 25, 50000)
print(f"Bonus of {e1.name} is {e1.get_bonus()}")

e2=Employee("Pallavi", 15, 400000)
print(f"Bonus of {e2.name} is {e2.get_bonus()}")