'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

剑指offer P145 面试题25
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        MergedHead = ListNode(0)
        if l1.val < l2.val:
            MergedHead = l1
            MergedHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            MergedHead = l2
            MergedHead.next = self.mergeTwoLists(l1, l2.next)
        return MergedHead
