class X:
	def __init__(self, x):
		self.x = x
		
	def check(self, x, y, z):
		return x + y + z == self.x
		
if __name__ == "__main__":
	x = int(input())
	y = int(input())
	z = int(input())
	
	checker = X(180)
	if checker.check(x, y, z):
		print("Yes")
	else:
		print("No")
