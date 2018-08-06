'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        lists = []
        while head != None:
            lists.append(head.val)
            head = head.next

        lists = sorted(lists)
        reshead = result = ListNode(lists[0])
        for i in range(1, len(lists)):
            node = ListNode(lists[i])
            result.next = node
            result = result.next
        return reshead
