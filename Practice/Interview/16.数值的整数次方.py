# -*- coding:utf-8 -*-

# 看似简单，但是情况要考虑周全
def Pow(base,exponent):
	if exponent == 0:
		return 1
	elif exponent > 0:
		ans = base
		for i in range(exponent-1):
			ans *= base
		return ans
	else:
		if base == 0:
			return 'Error!'
		else:
			ans = base
			for i in range(-exponent-1):
				ans *= base
			return 1/ans

# 对算法效率进行优化，采用递归，同时用位运算代替乘除运算及求余运算
# 但是不能处理底数为浮点数的运算
def Pow2(base,exponent):
	if exponent == 0:
		return 1
	elif exponent == 1:
		return base
	elif exponent > 1:
		ans = Pow2(base, exponent>>1)			# 右移代替整除
		ans *= ans
		if exponent & 1 == 1:					# 用位运算判断奇偶
			ans *= base
		return ans
	else:
		if base == 0:
			return 'Error!'
		ans = Pow2(base, (-exponent))
		return 1.0/ans

if __name__ == '__main__':
	test = [(2,3),(0,-5),(-2,-3),(0.5,2)]
	for base,exponent in test:
		print('base =', base, ',exponent =', exponent)
		print(Pow(base, exponent), end='\t')
		print(Pow2(base, exponent))