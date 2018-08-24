# -*- coding:utf-8 -*-

# 类似快排的思路
def OddEvenSort(nums):
	odd,even = 0,len(nums)-1
	flag1,flag2 = 0,0
	while odd < even:
		if flag1 and flag2:
			nums[odd],nums[even] = nums[even],nums[odd]
			flag1,flag2 = 0,0
		if nums[odd] & 1 == 1:
			odd += 1
		else:
			flag1 = 1
		if nums[even] & 1 == 0:
			even -= 1
		else:
			flag2 = 1
	return nums

# 保持奇数和奇数、偶数和偶数之间的相对位置不变
def OddEvenSort2(nums):
	flag = -1
	for i in range(len(nums)):
		if nums[i] & 1:
			if flag >= 0:
				temp = nums[i]
				for j in range(i,flag,-1):
					nums[j] = nums[j-1]
				nums[flag] = temp
				flag = flag+1
		elif flag < 0:
				flag = i
	return nums

if __name__ == '__main__':
	test = [[1,2,3,4,5,6,7],[2,4,1,3,5],[1,3,5,2,4],[2,3,4,5,6]]
	for nums in test:
		print("Before Sort:",nums)
		nums1 = OddEvenSort(nums.copy())
		print("After Sort:", nums1)
		nums2 = OddEvenSort2(nums.copy())
		print("After Sort:", nums2)