class X:
	def __init__(self, x):
		self.x = x
		
	def check(self, x, y, z):
		return x + y + z == self.x
