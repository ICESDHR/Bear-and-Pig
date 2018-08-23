# -*- coding:utf-8 -*-

class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

def MirrorBiTree(tree):
	if tree:
		tree.left,tree.right = MirrorBiTree(tree.right),MirrorBiTree(tree.left)
	return tree

def BuildTree():
	root = BinaryTreeNode(0)
	node1 = BinaryTreeNode(1)
	node2 = BinaryTreeNode(2)
	node3 = BinaryTreeNode(3)
	node4 = BinaryTreeNode(4)
	node5 = BinaryTreeNode(5)
	# root.left,root.right = node1,node2
	# node1.left,node1.right = node3,node4
	# node4.right = node5
	root.left = node1
	node1.left = node3
	node3.right = node5
	return root

def PrintTree(root):
	if root:
		PrintTree(root.left)
		print(root.value)
		PrintTree(root.right)

# 层次遍历
# def PrintTree(root):
# 	i = 1
# 	stack = [(root, 1)]
# 	while stack:
# 		current = stack.pop(0)
# 		if current[1] > i:
# 			print()
# 			i = i+1
# 		print(current[0].value,end=' ')
# 		if current[0].left:
# 			stack.append((current[0].left, current[1]+1))
# 		if current[0].right:
# 			stack.append((current[0].right, current[1]+1))
# 	print('\n')

if __name__ == '__main__':
	tree = BuildTree()
	PrintTree(tree)
	print('After Mirror:')
	MirrorBiTree(tree)
	PrintTree(tree)
