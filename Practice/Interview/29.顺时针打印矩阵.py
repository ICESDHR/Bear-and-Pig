# -*- coding:utf-8 -*-

def PrintMatrix(matrix):
	if matrix:
		for num in matrix[0]:
			print(num,end=' ')
		if len(matrix) > 1:
			for i in range(1,len(matrix)-1):
				print(matrix[i][-1],end=' ')
			for num in matrix[-1][::-1]:
				print(num,end=' ')
			if len(matrix[0]) > 1:
				for i in range(len(matrix)-2,0,-1):
					print(matrix[i][0],end=' ')
				if len(matrix) > 2 and len(matrix[0]) > 2:
					PrintMatrix([l[1:-1] for l in matrix[1:-1]])


if __name__ == '__main__':
	test = [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[1,2],[3,4],[5,6],[7,8],[9,10]],[[1,2,3,4]],[[1],[2],[3],[4]],[[1]]]
	for matrix in test:
		print('Matrix:')
		PrintMatrix(matrix)
		print()