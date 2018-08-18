# -*- coding:utf-8 -*-

# 时间复杂度为O(1)，此时不用找到待删除节点的前一个节点，但是要注意处理末节点
class ListNode:
	def __init__(self,val):
		self.value = val
		self.next = None

def DeleteNode(root,node):
	if node:
		if node.next:
			node.value = node.next.value
			node.next = node.next.next
		else:
			parent = root
			while parent.next != node:
				parent = parent.next
			parent.next = None

def Print(root):
	temp = root
	while temp:
		print(temp.value)
		temp = temp.next

if __name__ == '__main__':
	root = ListNode(0)
	node1 = ListNode(1)
	root.next = node1
	node2 = ListNode(2)
	node1.next = node2
	node3 = ListNode(3)
	node2.next = node3
	node4 = ListNode(4)
	node3.next = node4
	DeleteNode(root,node2)
	print("Delete Node2:")
	Print(root)
	DeleteNode(root, node4)
	print("Delete Node4:")
	Print(root)
	DeleteNode(root, None)
	print("Delete None:")
	Print(root)
	DeleteNode(root, root)
	print("Delete None:")
	Print(root)
