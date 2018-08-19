# -*- coding:utf-8 -*-

# 测试用例想不那么全
def IsDigit(string):
	if len(string) == 0:
		return False
	if string[0] == '-' or string[0] == '+' or string[0] == '.':
		string = string[1:]
	# flag1 表示E、e是否出现；flag2表示小数点是否出现；flag3表示E、e后是否符合标准
	flag1,flag2,flag3 = 0,0,0
	for i in range(len(string)):
		if string[i] < '0' or string[i] > '9':
			if (string[i] == 'E' or string[i] == 'e') and flag1 == 0 and i:
				flag1,flag3 = 1,1
			elif string[i] == '.' and flag1==0 and flag2 == 0:
				flag2 = 1
			else:
				if flag3 == 1 and string[i] == '-':
					flag3 = 2
				else:
					return False
		elif flag3 > 0:
			flag3 = 0
	if flag3 != 0:
		return False
	return True

def IsInt(string):
	flag = 0
	for i in range(len(string)):
		if string[i] > '9' or string[i] < '0':
			break
		flag = i+1
	if flag < 1:
		return False,string
	return True,string[flag:]

def IsFloat(string):
	flag,flag1 = -1,-1
	for i in range(len(string)):
		if string[i] > '9' or string[i] < '0':
			if string[i] == '.' and flag and i:
				flag = 0
				continue
			else:
				break
		flag1 = i+1
	if flag1 < 1:
		return False,string
	return True,string[flag1:]

# 按剑指offer的思路将字符串分部分讨论，但是写的很烂
def IsNumeric(string):
	if len(string) == 0:
		return False
	if string[0] == '-' or string[0] == '+':
		string = string[1:]
	if not IsInt(string)[0]:
		return False
	string = IsInt(string)[1]
	if len(string) and string[0] == '.':
		string = IsInt(string[1:])[1]
	if len(string) > 1 and (string[0] == 'e' or string[0] == 'E'):
		if string[1] == '-':
			string = string[1:]
		if not IsInt(string[1:])[0]:
			return False
		string = IsInt(string[1:])[1]
	if len(string) == 0:
		return True
	return False

# 使用python内置函数辅助判断
def Trick(s):
	try:
		float(s)
		if s[0:2] != '-+' and s[0:2] != '+-':
			return True
		else:
			return False
	except:
		return False

if __name__ == '__main__':
	test = ['+123','12e3','3.14159','-1E-6','20.','2q3','3e','12e1.5','+-5','1.2.3','e2','']
	for string in test:
		print('string:', string)
		if IsDigit(string):
			print('Bingo~')
		else:
			print('T_T')
		if IsNumeric(string):
			print('Bingo~')
		else:
			print('T_T')
		if Trick(string):
			print('Bingo~')
		else:
			print('T_T')