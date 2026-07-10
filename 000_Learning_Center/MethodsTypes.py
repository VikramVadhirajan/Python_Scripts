class Student:
	"This is the doc string defines about the class "
	college_name= "SASTRA" # Static Variables same for all the object in the class
	Director="Vaidhya"
	def __init__ (self, student_name, student_rollnumber):
		self.student_name=student_name # Instance Variable 
		self.student_rollnumber	= student_rollnumber  # Instance Variable

	def m1(self):
		x=10 # x is the local variable
		for i in range (x): # i is the local variable
			print (i)

	def getStudentInfo(self): #Instance Method since we are using instance variable  
		print("Student Name", self.student_name)
		print ("Student Rollno", self.student_rollnumber)


	@classmethod # Decorator to define the what method it is. Here i said class method. 

	def getCollegeInfo(cls): # Class method as we use a static Variable or class level variable.
		print("College Name is: ",cls.college_name) #cls. will allow us to access static variables. 
		print("Director Name is: ",cls.Director)


	@staticmethod # Decorator to define the what method it is. Here i said class method. 

	def getAverage(a,b,c):
		
		print("Average: ",(a+b+c)/3)


s=Student("Durga", 101)

s.getStudentInfo()
print()
Student.getCollegeInfo() # No need to call with the object as there is nothing related to the object. 
print()
Student.getAverage(90,50,70) # No need to call with the object as there is nothing related to the object. 
print(s.__dict__)