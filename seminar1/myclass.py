class Person:
	def __init_(self,Height=300, Weight=150):
		self.Height=Height
		self.Weight=Weight

	def info(self):
		print("Height is", self.Height)
		print("Weight is", self.Weight)

	def set_info(self,Height, Weight):
		self.Height=Height
		self.Weight=Weight
