class errnumber:
	def __init__(self, value, error):
		self.value = float(value)
		self.error = float(error)

	def __add__(self, other):
		new_value = self.value + other.value
		new_error = (self.error**2 + other.error**2)**.5
		return errnumber(new_value, new_error)
	
	def __sub__(self, other):
		new_value = self.value - other.value
		new_error = (self.error**2 + other.error**2)**.5
		return errnumber(new_value, new_error)

	def __mul__(self, other):
		new_value = self.value * other.value
		new_error = new_value*((self.error/self.value)**2 + (other.error/other.value)**2)**.5
		return errnumber(new_value, new_error)

	def __truediv__(self, other):
		new_value = self.value / other.value
		new_error = new_value*((self.error/self.value)**2 + (other.error/other.value)**2)**.5
		return errnumber(new_value, new_error)
	
	def __repr__(self):
		return str(self.value) +' ± ' + str(self.error)