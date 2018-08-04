#面试问到该题的话先问是不是二叉查找树，如果是的话就能根据大小关系方便的找到间235题
#如果不是二叉查找树则用下面的方法


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q):
        return root
    left, right = [lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
    if left and right: #如果左右都不空说明两个值分别存在左右子树中
        return root
    if not left:#如果有节点为空说明两个值都在左子树中
        return right
    if not right:
        return left
