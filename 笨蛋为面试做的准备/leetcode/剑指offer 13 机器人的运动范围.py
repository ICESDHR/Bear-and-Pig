# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        assistMatrix = [True] * rows * cols
        return self.movingCountPoint(threshold, rows, cols, 0, 0, assistMatrix)

    def movingCountPoint(self, threshold, rows, cols, i, j, assistMatrix):
        index = i * cols + j
        if i < 0 or i >= rows or j < 0 or j >= cols or assistMatrix[index] == False :
            return 0
        if self.check(i, j, threshold):
            assistMatrix[index] = False
            return 1 + self.movingCountPoint(threshold, rows, cols, i - 1, j, assistMatrix) \
                    + self.movingCountPoint(threshold, rows, cols, i + 1, j, assistMatrix) \
                    + self.movingCountPoint(threshold, rows, cols, i, j - 1, assistMatrix) \
                    + self.movingCountPoint(threshold, rows, cols, i, j + 1, assistMatrix)
        else:
            return 0

    def check(self, i, j, threshold):
        temp = 0
        while i > 0:
            temp += i %10
            i = i // 10
        while j > 0:
            temp += j % 10
            j = j // 10
        if temp <= threshold:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(5, 10, 10))