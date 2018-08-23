# -*- coding:utf-8 -*-

class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

def SubTree(tree1,tree2):
	if tree1 and tree2:
		if tree1.value != tree2.value:
			return SubTree(tree1.left,tree2) | SubTree(tree1.right,tree2)
		else:
			return SubTree(tree1.left,tree2.left) & SubTree(tree1.right,tree2.right)
	elif tree2:
		return False
	return True

def BuildTree1():
	root = BinaryTreeNode(0)
	node1 = BinaryTreeNode(1)
	node2 = BinaryTreeNode(2)
	node3 = BinaryTreeNode(3)
	node4 = BinaryTreeNode(4)
	node5 = BinaryTreeNode(5)
	root.left,root.right = node1,node2
	node1.left,node1.right = node3,node4
	node4.right = node5
	# root.left = node1
	# node1.left = node3
	# node3.right = node5
	return root

def BuildTree2():
	root = BinaryTreeNode(1)
	node1 = BinaryTreeNode(3)
	node2 = BinaryTreeNode(4)
	root.left, root.right = node1, node2
	# root.left = node1
	return root

if __name__ == '__main__':
	tree1 = BuildTree1()
	tree2 = BuildTree2()
	print(SubTree(tree1,tree2))