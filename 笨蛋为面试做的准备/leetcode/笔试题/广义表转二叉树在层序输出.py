class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build(s, len):
    sta = []
    left = 1
    right = 2
    flag = 0
    index = 0
    rootnode = None
    currnode = None
    while index < len:
        c = s[index]
        if c == "(":
            flag = left
            sta.append(currnode)
        elif c == ",":
            flag = right
        elif c == ")":
            sta.pop()
        else:
            currnode = TreeNode(c)
            if rootnode == None:
                rootnode = currnode
            elif flag == left:
                sta[-1].left = currnode
            elif flag == right:
                sta[-1].right = currnode
        index += 1
    return rootnode


def levelOrder(root):
    # write your code here
    if root is None: return []
    stack = [root]
    yy = []
    # none就出
    while stack:
        y = []
        # 出栈
        # 每一层
        for i in range(len(stack)):
            current = stack.pop(0)
            y.append(current.val)
            if current.left:
                # 入栈
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        yy.append(y)
    return yy


def pre_visit(root):
    if root:
        print(root.val)
        pre_visit(root.left)
        pre_visit(root.right)


if __name__ == "__main__":
    # print(build("A(B(D),D)", len("A(B(D),D)")))
    # build("A(B(D),D)", len("A(B(D),D)"))
    lst = levelOrder(build("1(2(4,5(7,8)),3(6))", len("1(2(4,5(7,8)),3(6))")))
    for line in lst:
        for item in line:
            print(item, end=' ')
        print()
