'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 均不为空。


'''
def findMedianSortedArrays(nums1, nums2):
    res = nums1 + nums2
    res.sort()
    n = len(res) // 2  # //表示整数除法
    return res[n] if len(res) % 2 == 1 else (res[n] + res[n - 1]) / 2

if __name__=="__main__":
    print(findMedianSortedArrays([1, 3], [2]))