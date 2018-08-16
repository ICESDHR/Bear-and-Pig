# -*- coding:utf-8 -*-

# 借助了python中二进制函数bin()将数字转化为二进制字符串
def NumberOf1(n):
	if n < 0:
		n = n & 0xffffffff
	return bin(n).count('1')

# 常规除以2或和1做与运算再每次右移1位的方法对于负数不可行;
# python没有大数限制，所以不能将1每次左移和原数做与运算；
# 减1再和原数做与运算，即可把最右一个1去除
def NumberOf12(n):
	ans = 0
	if n < 0:
		n = n & 0xffffffff
	while n:
		n = (n-1) & n
		ans += 1
	return ans

if __name__ == '__main__':
	test = [-5,-1,0,5,8]
	for n in test:
		print('n =',n)
		print(NumberOf1(n),end='\t')
		print(NumberOf12(n), end='\t')