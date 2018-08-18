# -*- coding:utf-8 -*-

# 输入n，打印从1到最大的n位数

def Print(pre,n):
	if n < 1:
		if pre > '0':
			print(int(pre))
		return
	for i in range(10):
		Print(pre+str(i),n-1)

if __name__ == '__main__':
	test = [3, -1, 0]
	for n in test:
		print('n =',n)
		Print('', n)