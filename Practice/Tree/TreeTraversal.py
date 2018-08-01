# -*- coding:utf-8 -*-
# 二叉树的7种遍历
# TODO 中序后序非递归遍历需要再认真看看

class TreeNode:
	def __init__(self,value=None,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

preRecur = []
inRecur = []
posRecur = []

def PreRecurTraversal(root):
	if root:
		preRecur.append(root.value)
		PreRecurTraversal(root.left)
		PreRecurTraversal(root.right)

def PreNonRecurTraversal(root):
	ans = []
	stack = [root]
	while stack:
		top = stack.pop()
		if top:
			ans.append(top.value)
			stack.append(top.right)
			stack.append(top.left)
	return ans

def PreNonRecurTraversal2(root):
	ans,stack = [],[root]
	while stack:
		top = stack.pop()
		while top:
			ans.append(top.value)
			stack.append(top.right)
			top = top.left
	return ans

def InRecurTraversal(root):
	if root:
		InRecurTraversal(root.left)
		inRecur.append(root.value)
		InRecurTraversal(root.right)

def InNonRecurTraversal(root):
	ans,stack = [],[]
	top = root
	while top or stack:
		while top:
			stack.append(top)
			top = top.left
		if stack:
			top = stack.pop()
			ans.append(top.value)
			top = top.right
	return ans


def PostRecurTraversal(root):
	if root:
		PostRecurTraversal(root.left)
		PostRecurTraversal(root.right)
		posRecur.append(root.value)

def PostNonRecurTraversal(root):
	ans,stack = [],[]
	markNode = None
	top = root
	while top or stack:
		while top:
			stack.append(top)
			top = top.left
		if stack:
			top = stack.pop()
			if not top.right or top.right is markNode:
				ans.append(top.value)
				markNode = top
				top = None
			else:
				stack.append(top)
				top = top.right
	return ans

# 相当于用了两个栈
def PostNonRecurTraversal2(root):
	ans,stack = [],[]
	top = root
	while top or stack:
		while top:
			ans.append(top.value)
			stack.append(top)
			top = top.right
		if stack:
			top = stack.pop()
			top = top.left
	return ans[::-1]


def LevelTraversal(root):
	ans,queue = [],[root]
	while queue:
		top = queue.pop(0)
		if top:
			ans.append(top.value)
			queue.append(top.left)
			queue.append(top.right)
	return ans

if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)
	print("PreTraversal:")
	PreRecurTraversal(root)
	print(preRecur)
	print(PreNonRecurTraversal(root))
	print("InTraversal:")
	InRecurTraversal(root)
	print(inRecur)
	print(InNonRecurTraversal(root))
	print("PostTraversal:")
	PostRecurTraversal(root)
	print(posRecur)
	print(PostNonRecurTraversal(root))
	print("LevelTraversal:")
	print(LevelTraversal(root))
	# 需要用普通二叉树、特殊二叉树(所有节点均无左子节点或均无右子节点或只有根节点)、空指针分别测试
