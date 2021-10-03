class Employee():
	def __init__(self,last_name,first_name,annual_salary):
		self.last_name=last_name
		self.first_name=first_name
		self.annual_salary=annual_salary
	def give_raise(self,increment=5000):
		self.annual_salary=self.annual_salary+increment