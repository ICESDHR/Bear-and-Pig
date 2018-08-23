# -*- coding:utf-8 -*-

class ListNode:
	def __init__(self,value):
		self.value = value
		self.next = None

# 没思路
def ReverseList(root):
	pNode,parent,pHead = root,None,None
	while pNode:
		child = pNode.next
		if child is None:
			pHead = pNode
		pNode.next = parent
		parent = pNode
		pNode = child
	return pHead

# 递归方法，需要返回两个值
def ReverseList2(root):
	if root and root.next:
		pHead,parent = ReverseList2(root.next)
		parent.next = root
		root.next = None
		return pHead,root
	return root,root

def Build():
	root = ListNode(0)
	node1 = ListNode(1)
	root.next = node1
	node2 = ListNode(2)
	node1.next = node2
	node3 = ListNode(3)
	node2.next = node3
	node4 = ListNode(4)
	node3.next = node4
	return root

def Print(root):
	temp = root
	while temp:
		print(temp.value)
		temp = temp.next

if __name__ == '__main__':
	test = []
	root = Build()
	print('The List is:')
	Print(root)
	print('After reverse:')
	Print(ReverseList(root))
	# pHead,parent = ReverseList2(root)
	# Print(pHead)
