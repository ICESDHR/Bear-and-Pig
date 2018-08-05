'''
如果正整数可以被 A 或 B 整除，那么它是神奇的。

返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。



示例 1：

输入：N = 1, A = 2, B = 3
输出：2
示例 2：

输入：N = 4, A = 2, B = 3
输出：6
示例 3：

输入：N = 5, A = 2, B = 4
输出：10
示例 4：

输入：N = 3, A = 6, B = 4
输出：8


提示：

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
'''

import sys
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def nthMagicalNumber(self, N, A, B):
        """
        建立一个大区间，通过二分法来求解，大区间的mid，可以知道mid左边有mid/A个A，mid/B个B ，mid/G个AB的最小公倍数，
        mid/A+mid/B-mid/g就代表mid左边有多少个满足条件的数。然后二分法求解，直到找到一定个数的满足条件的数。
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        g = A*B//self.gcd(A,B)
        low = 0
        high = sys.maxsize
        while(low < high):
            mid = (low+high) // 2
            t = mid//A + mid//B - mid//g
            if t < N:
                low = mid+1
            else:
                high = mid
        return high % (10**9+7)

if __name__ == "__main__":
    solution = Solution()
    print(solution.nthMagicalNumber(3, 6, 4))