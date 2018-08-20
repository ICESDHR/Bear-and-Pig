# -*- coding:utf-8 -*-

# 代码的鲁棒性要增强，要考虑空指针、越界等情况
class ListNode:
	def __init__(self,value):
		self.value = value
		self.next = None

def FindK(root,k):
	count = 0
	pfast, pslow = root, root
	while pfast:
		count += 1
		pfast = pfast.next
		if count > k:
			pslow = pslow.next
	if count >= k > 0:
		return pslow.value
	else:
		return 'Error!'

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
	root = Build()
	Print(root)
	print('The 0th node to tail is:', FindK(root,0))
	print('The 1th node to tail is:', FindK(root,1))
	print('The 3th node to tail is:', FindK(root,3))
	print('The 5th node to tail is:', FindK(root,5))
	print('The 7th node to tail is:', FindK(root,7))
	print('The 7th node to tail is:', FindK(None,7))