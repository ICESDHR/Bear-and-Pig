'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        三指针法
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        i = m-1
        j = n-1
        while j >= 0:
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[index] = nums1[i]
                    i -= 1
                else:
                    nums1[index] = nums2[j]
                    j -= 1
            index -= 1


if __name__ == "__main__":
    solution = Solution()
    num1 = [2, 0]
    solution.merge(num1, 1, [1], 1)
    print(num1)