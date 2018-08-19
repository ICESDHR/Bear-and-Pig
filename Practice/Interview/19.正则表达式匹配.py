# -*- coding:utf-8 -*-

# 采用递归的思想，各个情况需要考虑周全
def Match(string,pattern):
	if len(string) == 0 and len(pattern) == 0:
		return True
	elif len(pattern) == 0:
		return False
	elif len(string) == 0:
		if len(pattern) > 1 and pattern[1] == '*':
			return Match(string, pattern[2:])
		return False
	else:
		if string[0] == pattern[0] or pattern[0] == '.':
			if len(pattern) > 1 and pattern[1] == '*':
				return Match(string[1:], pattern) or Match(string, pattern[2:])
			return Match(string[1:],pattern[1:])
		else:
			if len(pattern) > 1 and pattern[1] == '*':
				return Match(string, pattern[2:])
			return False

if __name__ == '__main__':
	test = [('aaa','a.a'),('aaa','aaa*a'),('aaa','ab*ac*a'),('abc','a.*'),('aaa','ab*a'),('','a*')]
	for string,pattern in test:
		print('string:',string,'\tpattern:',pattern)
		if Match(string,pattern):
			print('Bingo~')
		else:
			print('T_T')
