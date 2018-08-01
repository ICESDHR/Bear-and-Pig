# -*- coding:utf-8 -*-

# 中序遍历时二叉树的下一个节点
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# TODO 这一题的细节都没考虑到
def NextNode(pNode):
    # 若给定节点的右子树存在，则中序遍历的下一个节点为右子树的最左节点
    if pNode.right:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    else:
        # 若给定节点右子树不存在，则中序遍历的下一个节点为左子树包含该节点的父节点
        while pNode.next:
            parent = pNode.next
            if parent.left == pNode:
                return parent
            else:
                pNode = parent
        return None
