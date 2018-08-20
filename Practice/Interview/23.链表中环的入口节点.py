# -*- coding:utf-8 -*-

# 没有思路，应该先判断是否存在环，然后再寻找环的入口节点
class ListNode:
	def __init__(self,value):
		self.value = value
		self.next = None

def HasCircle(root):
	flag = 0
	pfast, pslow = root, root
	while pfast:
		pfast = pfast.next
		if pfast == pslow:
			flag = 1
			break
		if pfast:
			pfast, pslow = pfast.next, pslow.next
	if flag == 0:
		return None
	return pfast

def CountCircle(pcircle):
	length = 1
	pfast = pcircle
	while pfast.next != pcircle:
		length += 1
		pfast = pfast.next
	return length

def EntryNode(root):
	pcircle = HasCircle(root)
	if pcircle:
		count = 0
		pfast, pslow = root, root
		length = CountCircle(pcircle)
		while pfast:
			count += 1
			pfast = pfast.next
			if count > length:
				pslow = pslow.next
			if pfast == pslow:
				return pslow.value
	return None

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
	node4.next = root
	return root

def Print(root,k):
	temp = root
	for i in range(k):
		print(temp.value)
		temp = temp.next

if __name__ == '__main__':
	root = Build()
	Print(root,6)
	print("The entry node of circle is:",EntryNode(root))