# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def PrintListFromTailToHead(listNode):
    if listNode != None:
        temp = [listNode.val]
        nodes = listNode
    else:
        return []
    while nodes.next != None:
        temp.append(nodes.next.val)
        nodes = nodes.next
    return temp[::-1]

# 使用递归
def PrintListFromTailToHead2(listNode):
    if listNode != None:
        return PrintListFromTailToHead2(listNode.next)+[listNode.val]
    else:
        return []

if __name__ == '__main__':
    listNode = ListNode(5)
    listNode.next = ListNode(7)
    ans = PrintListFromTailToHead2(listNode)
    print(ans)
