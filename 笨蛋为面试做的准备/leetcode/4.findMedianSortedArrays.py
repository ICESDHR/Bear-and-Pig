def findMedianSortedArrays(nums1, nums2):
    res = nums1 + nums2
    res.sort()
    n = len(res) // 2  # //表示整数除法
    return res[n] if len(res) % 2 == 1 else (res[n] + res[n - 1]) / 2

if __name__=="__main__":
    print(findMedianSortedArrays([1, 3], [2]))