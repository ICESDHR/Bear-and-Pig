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
