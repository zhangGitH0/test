class calculator():	
	def add (self, num1, num2):
		return num1 + num2

	def subtract (self, num1, num2):
		return num1 - num2

	def divide (self, num1, num2):
		if num2 == 0:
			return 0
		return num1 / num2

if __name__ == "__main__":
	cal1 = calculator()
	print (cal1.add(1, 5))
	print (cal1.divide(10, 5))
