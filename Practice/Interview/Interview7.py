# -*- coding:utf-8 -*-

# 根据先序遍历和中序遍历重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def ReconstructBinaryTree(pre,mid):
    if len(pre) >= 1:
        node = TreeNode(pre[0])
        index = mid.index(pre[0])
        node.left = ReconstructBinaryTree(pre[1:index+1],mid[:index])
        node.right = ReconstructBinaryTree(pre[index+1:],mid[index+1:])
    else:
        node = None
    return node

# 层次遍历二叉树
def lookup(root):
    i = 1
    stack = [(root, 1)]
    while stack:
        current = stack.pop(0)
        if current[1] > i:
            print()
            i = i+1
        print(current[0].val,end=' ')
        if current[0].left:
            stack.append((current[0].left, current[1]+1))
        if current[0].right:
            stack.append((current[0].right, current[1]+1))


if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    mid = [4,7,2,1,5,3,8,6]
    root = ReconstructBinaryTree(pre,mid)
    lookup(root)
    # 需要用普通二叉树、特殊二叉树(所有节点均无左子节点或均无右子节点或只有根节点)、空指针分别测试
