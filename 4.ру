class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class Deque:


	def __init__(self):
		self.size = 0
		self.front = None
		self.back = None

	def push_back(self, value):
		n = Node(value)

		if self.is_empty():
			self.back = n
			self.front = n
			self.size += 1
			return

		n.next = self.back
		self.back.prev = n
		self.back = n
		self.size += 1

	def push_front(self, value):
		n = Node(value)

		if self.is_empty():
			self.back = n
			self.front = n
			self.size += 1
			return

		self.front.next = n
		n.prev = self.front
		self.front = n
		self.size += 1

	def pop_back(self):
		if self.is_empty():
			raise Exception("Deque is empty.")

		n = self.back
		if n.next is None:
			self.back = None
			self.size = 0
			return n.value

		self.back = n.next
		self.back.prev = None
		self.size -= 1
		return n.value

	def pop_front(self):
		if self.is_empty():
			raise Exception("Deque is empty.")

		n = self.front
		if n.prev is None:
			self.front = None
			self.size = 0
			return n.value

		self.front = n.prev
		self.front.next = None
		self.size -= 1
		return n.value

	def size():
		return self.size

	def is_empty(self):
		return self.size == 0

if __name__ == "__main__":
	deque = Deque()
	deque.push_back(1)
	deque.push_back(2)
	deque.push_back(3)

	print(deque.pop_back())
	print(deque.pop_front())
	print(deque.pop_back())
