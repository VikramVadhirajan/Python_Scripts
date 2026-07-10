class Test:
	def m1 (self):
		a=100 # local variable
		print(a)

	def m2(self):
		b=200
		print(b)
		#you cannot access a outiside m1 and similarly you cannot access b outside m2

t=Test()

t.m1()
t.m2()

