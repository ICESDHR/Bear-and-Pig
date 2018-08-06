# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        if res == []:
            return []
        res.sort()
        l = ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next

    def mergeKLists1(self, lists):
        """
        不如第一种
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1: return []

        head = ListNode(0)
        head.next = lists[0]
        for lst in lists[1:]:
            node = head
            item = lst
            while item and node.next:
                if node.next.val > item.val:
                    nodebak = node.next
                    node.next = ListNode(item.val)
                    node = node.next
                    node.next = nodebak
                    item = item.next
                else:
                    node = node.next
            if item:
                node.next = item
        return head.next
