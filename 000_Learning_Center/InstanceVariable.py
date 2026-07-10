class Test:
	def __init__(self): #Defining the instance variable within the constructor
		self.a=10
		self.b=20
		self.c=30
		self.d=40
		self.e=50
		self.f=60		

	def m1(self): #Defining the instance variable within the instance method
		self.z=30
		del self.a # Deleting the instance variable inside the class

t1=Test()
print(t1.__dict__) # shows the instance varialbe in the class 
t1.m1() 
del t1.b, t1.c # Deleting the instance variable outiside the class for a specific object. 
print(t1.z) # calling the instance variable outside class
print(t1.__dict__)
t2=Test()

t2.y=40 # defining the instance variable outside the Class
t2.x=50

print(t2.__dict__)


t3=Test()
t4=Test()
t3.a=888
t3.b=999
print(t3.__dict__)
print(t4.__dict__)

