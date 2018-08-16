# -*- coding:utf-8 -*-

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,node):
        self.stack1.append(node)
        print(node)

    # TODO 和答案想的不一样，自己想的是只存在栈1中，栈2辅助弹出；答案是将数据存在两个栈中，对于较长的栈答案较优化
    def pop(self):
        if len(self.stack1)+len(self.stack2) > 0:
            if len(self.stack2) == 0:
                while len(self.stack1) > 0:
                    self.stack2.append(self.stack1.pop())
            ans = self.stack2.pop()
            print(ans)
            return ans
        else:
            print("The queue is empty!")

if __name__ == '__main__':
    q = Queue()
    q.pop()
    q.push(2)
    q.pop()
