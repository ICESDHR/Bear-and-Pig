# -*- coding:utf-8 -*-

class Stack:
	def __init__(self):
		self.stack = []
		self.stack2 = []

	def push(self,value):
		self.stack.append(value)
		if self.stack2 and self.stack2[-1] < value:
			self.stack2.append(self.stack2[-1])
		else:
			self.stack2.append(value)

	def pop(self):
		temp = self.top()
		self.stack = self.stack[:-1]
		self.stack2 = self.stack2[:-1]
		return temp

	def top(self):
		if self.stack:
			return self.stack[-1]

	def min(self):
		if self.stack2:
			return self.stack2[-1]

if __name__ == '__main__':
	stack = Stack()
	stack.push(12)
	stack.push(2)
	stack.push(8)
	print(stack.min())
	print(stack.top())
	stack.pop()
	stack.push(5)
	print(stack.min())