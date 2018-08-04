# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        self.preOrder(root, lst)
        return lst

    def preOrder(self, root, lst):
        if root == None:
            return
        lst.append(root.val)
        if root.left != None:
            self.preOrder(root.left, lst)
        if root.right != None:
            self.preOrder(root.right, lst)
        return
