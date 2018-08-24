# -*- coding:utf-8 -*-

class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

def IsSymmetrical(tree1,tree2):
	if tree1 and tree2 and tree1.value == tree2.value:
		return IsSymmetrical(tree1.left,tree2.right) & IsSymmetrical(tree1.right,tree2.left)
	elif tree1 is None and tree2 is None:
		return True
	else:
		return False

def BuildTree():
	root = BinaryTreeNode(0)
	node1 = BinaryTreeNode(1)
	node2 = BinaryTreeNode(1)
	node3 = BinaryTreeNode(2)
	node4 = BinaryTreeNode(2)
	node5 = BinaryTreeNode(3)
	node6 = BinaryTreeNode(3)
	root.left,root.right = node1,node2
	# node1.left,node1.right = node3,node4
	# node4.right,node4.right = node5,node6
	node1.left = node3
	node3.left = node5
	node2.right = node4
	node4.right = node6
	return root

if __name__ == '__main__':
	tree = BuildTree()
	print(IsSymmetrical(tree,tree))