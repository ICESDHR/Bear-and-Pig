# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        left, right = 0, len(nums) - 1
        return self.helper(nums, left, right)

    def helper(self, A, left, right):
        if left <= right:
            mid = (left + right) // 2
            root = TreeNode(A[mid])
            root.left = self.helper(A, left, mid - 1)
            root.right = self.helper(A, mid + 1, right)
        else:
            return None
        return root
