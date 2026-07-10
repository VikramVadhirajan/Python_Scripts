import sys

class Customer:
	"""Customer class to describe bank operations"""

	BankName="HDFC"

	def __init__(self, custname, balance=0.0):
		self.custname=custname
		self.balance=balance

	def deposit(self, amount):
		self.balance+=amount
		print(f"Balance of {self.custname} after deposit:", self.balance)

	def withdraw(self, amount):
		if amount> self.balance:
			print("Insufficient funds cannot perform this operation")
			sys.exit()
		if self.balance-amount<1000:
			AllowedWithdraw=self.balance-1000
			print(f"Cannot withdraw minimum balance criteria doesnot meet you can withdraw only {AllowedWithdraw}")
			sys.exit()
		self.balance-=amount
		print(f"Balance of {self.custname} after withdraw:", self.balance)

print (f"Welcome to {Customer.BankName}")
name=input("Enter Your Name")
# Balance=float(input("Enter your balance"))
c1=Customer(name)
while True:
	print("_"*50)
	print('d-Deposit\nw-Withdraw \ne-Exit')
	option = input("Choose your option:")
	if option.lower()=="d":
		amount=float(input("enter the deposit amount:"))
		c1.deposit(amount)
	elif option.lower()=="w":
		amount=float(input("enter the withdraw amount:"))
		while amount % 500 !=0:
			print("Amount should be in multiples of 500")
			amount=float(input("enter the withdraw amount:"))
		c1.withdraw(amount)
	elif option.lower()=="e":
		print("Thanks for Banking with us.")
		sys.exit()
	else:
		print("invalid option please choose a valid option.")

