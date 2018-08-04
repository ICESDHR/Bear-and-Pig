class Solution:
    def climbStairs1(self, n):
        """
        最不好的超时了
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n-1)+self.climbStairs1(n-2)
    '''
    求斐波那契额数将第一个代码的n==2去掉
    将第二个代码的将fibNMinusOne改为fibNMinusOne=0
    '''
    def climbStairs(self, n):
        result = [0, 1]
        if n<2:
            return result[n]
        fibNMinusOne = 1
        fibNMinusTwo = 1
        fibN = 0
        for i in range(2, n+1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
        return fibN

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(3))