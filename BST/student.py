class Student:
	def __init__(self, last, first, ssn, email, age, retrieved = False):
		self.last = last
		self.first = first 
		self.ssn = ssn
		self.email = email
		self.age = age
		self.retrieved = retrieved

	def getAge(self):
		return int(self.age)

	def __str__(self):
		return self.first + " " + self.last + " " + self.ssn
	
	def __eq__(self, rhs):
		if rhs == None or rhs == False:
			return False
		return self.ssn == rhs.ssn

	def __ne__(self, rhs):
		if rhs == None or rhs == False:
			return False
		return self.ssn != rhs.ssn

	def __lt__(self, rhs):
		return self.ssn < rhs.ssn

	def __le__(self, rhs):
		return self.ssn <= rhs.ssn

	def __gt__(self, rhs):
		return self.ssn > rhs.ssn

	def __ge__(self, rhs):
		return self.ssn >= rhs.ssn

	def __int__(self):
		num = int(self.ssn.replace("-", ""))
		return num
