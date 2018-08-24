# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers):
        # write code here
        for i in range(len(numbers)):
            while(numbers[i] != i):
                if numbers[i] == numbers[numbers[i]]:
                    duplication = numbers[i]
                    print(duplication)
                    return True
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp

                # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
        return False

if __name__ == "__main__":
    solution = Solution()
    solution.duplicate([2,3,1,0,2,5,3])