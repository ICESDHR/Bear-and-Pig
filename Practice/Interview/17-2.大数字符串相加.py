# -*- coding:utf-8 -*-

# 考虑负数的情况好麻烦，写的好烂
def Add(num1,num2):
	ans = []
	flag1,flag2 = 0,1
	num1,num2 = str(num1),str(num2)
	if num1[0] == '-' and num2[0] == '-':
		flag1 = 1
		num1,num2 = num1[1:],num2[1:]
	elif num1[0] == '-':
		num1,num2 = num2,num1[1:]
		flag2 = -1
	elif num2[0] == '-':
		num2 = num2[1:]
		flag2 = -1

	maxlen = max(len(num1),len(num2))
	temp = 0
	for i in range(maxlen):
		if len(num1) > i:
			digit1 = ord(num1[-i]) - ord('0')
		else:
			digit1 = 0
		if len(num2) > i:
			digit2 = ord(num2[-i]) - ord('0')
		else:
			digit2 = 0
		count = digit1+flag2*(digit2+temp)
		if 0<= count <= 9:
			ans.append(str(count))
			temp = 0
		else:
			ans.append(str(count)[-1])
			temp = 1
	return flag1*'-' + temp*'1'+ ''.join(ans[::-1])

if __name__ == '__main__':
	test = [(666,55),(-999,-2222),(-77,333),(0,0)]
	for num1,num2 in test:
		print(Add(num1,num2))