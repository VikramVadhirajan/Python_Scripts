class Test:
	a=10 # Static variable

	def __init__(self):
		self.b=20 # instance Variable
		Test.c=100 # using class name hence Static Variable. 
		print("accessing static variable as Test.",Test.a) # acessing the
		print("accessing static variable as self.",self.a)

	def m1 (self):
		self.d=200
		Test.e=200
		print("accessing static variable as self.",self.a)
		print("accessing static variable as class name.",Test.a) # this is common practice

	@classmethod
	def m2 (cls):
		cls.g=50 # using cls variable hence Static Variable. 
		Test.f=40
		print("accessing static variable as cls.",cls.a)
		print("accessing static variable as class name.",Test.a) # this is common practice

	@staticmethod
	def m3 ():
		Test.h=60 

print(Test.a)
print(Test.__dict__)# Calling the class Test 
t=Test()
print(t.__dict__) # Calling the object t
# calling the test after calling the object. 
print(Test.__dict__)# Calling the class Test 
t.m1()
# calling the test after calling the instance method m1. 
print(Test.__dict__) 
# calling the class after calling the object method m2. 
Test.m2()
print(Test.__dict__) 
# calling the class after calling the static method m2. 
Test.m3()
print(Test.__dict__) 

Test.i=70 # dreating outside of the class. 
print(Test.__dict__) 

# ___________________________________________________________________________________________________________________

print("*"*100)
print("Modifying the Static Variable")
print("*"*100)

class Test:
	a=10

	@classmethod
	def m1(cls):
		cls.a=20
		print("the static variable is changed using cls")

	@staticmethod
	def m2():
		Test.a=30

Test.m1()
Test.m2()
print(Test.a)


# ___________________________________________________________________________________________________________________

print("*"*100)
print("Having same name for static and Object level variable.")
print("*"*100)

class Test:
	a=10

	def m1(self):
		self.a=888

t=Test()
t.m1()
print(Test.a) # This is the Static Variable
print(t.a) # This is the Instance Variable


# ___________________________________________________________________________________________________________________

print("*"*100)
print("New instance variable creation by accessing object reference t1.")
print("*"*100)

class Test:
	x=10
	def __init__(self):
		self.y=20


t1=Test()
t2=Test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
t1.x=888 # This will be a new instance variable for t1 
t1.y=999 # this is already an instance variable which is updated now to 999
Test.x=100 # Updating the static variable through class name. 
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)

# ___________________________________________________________________________________________________________________

print("*"*100)
print("New instance variable creation by accessing object reference t1.")
print("*"*100)

class Test:
	x=10
	def __init__(self):
		self.y=20

	@classmethod
	def m1 (cls):
		cls.x=888 # This is changing the static variable. and unless we call 
		cls.y=999


t1=Test()
t2=Test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
t1.m1() 
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)

# ___________________________________________________________________________________________________________________

print("*"*100)
print("Deleting the static variable")
print("*"*100)

class Test:
	a=10

	@classmethod
	def m1 (cls):
		del cls.a

print(Test.__dict__)
Test.m1()
print(Test.__dict__)

print("*"*100)

class Test:
	a=10

	def __init__(self):
		Test.b=20
		del Test.a

	def m1(self):
		Test.c=30
		del Test.b

	@classmethod
	def m2(cls):
		cls.d=40
		del Test.c 

	@staticmethod
	def m3():
		Test.e=50
		del Test.d

print(Test.__dict__)

t=Test() #constructor is executed. 
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
del Test.e 
print(Test.__dict__)
del Test.f
print(Test.__dict__)


print("*"*100)

class Test:
	x=10
	def __init__(self):
		self.y=20

t1=Test()
t2=Test()
print("t1:", t1.x, t1.y)
print("t2:", t2.x, t2.y)
Test.x=888
t1.y=999
print("t1:", t1.x, t1.y)
print("t2:", t2.x, t2.y)