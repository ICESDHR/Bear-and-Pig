# -*- coding:utf-8 -*-

class ListNode:
	def __init__(self,val):
		self.value = val
		self.next = None

def DelDupNode(root):
	temp = root
	while temp and temp.next:
		if temp.value == temp.next.value:
			temp.value = temp.next.value
			temp.next = temp.next.next
		else:
			temp = temp.next

def Bulid():
	root = ListNode(0)
	node1 = ListNode(0)
	root.next = node1
	node2 = ListNode(1)
	node1.next = node2
	node3 = ListNode(1)
	node2.next = node3
	node4 = ListNode(2)
	node3.next = node4
	node5 = ListNode(3)
	node4.next = node5
	node6 = ListNode(3)
	node5.next = node6
	return root

def Print(root):
	temp = root
	while temp:
		print(temp.value)
		temp = temp.next

if __name__ == '__main__':
	root = Bulid()
	DelDupNode(root)
	Print(root)
	temp = None
	DelDupNode(temp)
	Print(temp)