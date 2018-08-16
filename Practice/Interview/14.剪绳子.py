# -*- coding:utf-8 -*-
from functools import reduce

# 已知绳子长度，将其剪为若干段，求能剪出的最大长度之积

# 解法1：使用数学知识辅助，直接得到结果
def CutRope1(n):
	ans = [0]
	for i in range(2,n+1):
		average = n//i
		if n%i == 0:
			temp = [average for j in range(i)]
		else:
			temp = [average for j in range(i-n%i)] + [average+1 for j in range(n%i)]
		ans.append(reduce(lambda a, b: a*b, temp))
	return max(ans)

# 解法2：使用动态规划
def CutRope2(n):
	ans = [0,1]
	if n < 3:
		return ans[n-1]
	for i in range(2,n):
		maxmium = 0
		for j in range(i):
			temp = max(ans[j],j+1)*max(ans[i-j-1],(i-j))
			if temp > maxmium:
				maxmium = temp
		ans.append(maxmium)
	return ans[-1]

if __name__ == '__main__':
	test = [1,2,3,4,5]
	for n in test:
		print('n =',n)
		print(CutRope1(n),end='\t')
		print(CutRope2(n))