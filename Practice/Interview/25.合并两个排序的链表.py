# -*- coding:utf-8 -*-

# 看似简单其实写了好久没写出来= =
# 对于一个函数体内的链表指针，令pNode=root，则pNode修改时root也会随之修改
class ListNode:
	def __init__(self,value):
		self.value = value
		self.next = None

def Merge(root1,root2):
	if root1 and root2:
		if root1.value < root2.value:
			root1.next = Merge(root1.next, root2)
			return root1
		else:
			root2.next = Merge(root1, root2.next)
			return root2
	elif root1:
		return root1
	else:
		return root2

def Build1():
	root = ListNode(0)
	node1 = ListNode(2)
	root.next = node1
	node2 = ListNode(3)
	node1.next = node2
	node3 = ListNode(7)
	node2.next = node3
	node4 = ListNode(11)
	node3.next = node4
	return root

def Build2():
	root = ListNode(1)
	node1 = ListNode(4)
	root.next = node1
	node2 = ListNode(5)
	node1.next = node2
	node3 = ListNode(9)
	node2.next = node3
	node4 = ListNode(10)
	node3.next = node4
	return root

def Print(root):
	temp = root
	while temp:
		print(temp.value)
		temp = temp.next

if __name__ == '__main__':
	root1 = Build1()
	root2 = Build2()
	Print(Merge(root1,root2))
