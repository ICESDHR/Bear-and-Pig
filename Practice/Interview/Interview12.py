# -*- coding:utf-8 -*-

# 矩形中是否存在包含某字符串的路径
# TODO 需要好好看看，自己想了好久才想出来一个很麻烦的方案
def hasPath(matrix, rows, cols, path):
    for i, s in enumerate(matrix):
        if s==path[0] and visit([(i//cols, i%cols)], matrix, rows, cols, path):
            return True
    return False

def visit(ans, matrix, rows, cols, path):
    if len(ans)==len(path):
        return True
    i,j = ans[-1]
    nex = [(ii,jj) for ii,jj in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
           if 0<= ii <rows and 0<= jj <cols and (ii,jj) not in ans and matrix[ii*cols +jj]==path[len(ans)]]
    return sum([visit(ans+[x], matrix, rows, cols, path) for x in nex])


def HasPath(matrix, rows, cols, path):
    for i in range(rows):
        for j in range(cols):
            if matrix[i*cols+j] == path[0]:
                if HasChild(matrix, rows, cols, path[1:], [(i, j)]):
                    return True
    return False

def HasChild(matrix, rows, cols, path, flag):
    if len(path) == 0:
        return True
    row,col = flag[-1]
    if row+1 < rows and matrix[(row+1)*cols+col] == path[0] and (row+1,col) not in flag:
        if HasChild(matrix, rows, cols, path[1:], flag+[(row+1,col)]):
            return True
    if row-1 >= 0 and matrix[(row-1)*cols+col] == path[0] and (row-1,col) not in flag:
        if HasChild(matrix, rows, cols, path[1:], flag+[(row-1,col)]):
            return True
    if col+1 < cols and matrix[row*cols+col+1] == path[0] and (row,col+1) not in flag:
        if HasChild(matrix, rows, cols, path[1:], flag+[(row,col+1)]):
            return True
    if col-1 >= 0 and matrix[row*cols+col-1] == path[0] and (row,col-1) not in flag:
        if HasChild(matrix, rows, cols, path[1:], flag+[(row,col-1)]):
            return True
    return False


if __name__ == '__main__':
    matrix = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
    rows,cols = 5,8
    paths = ["SLHECCEIDEJFGGFIE","ABCB"]
    for path in paths:
        if HasPath(matrix, rows, cols, path):
            print("Bingo")
        else:
            print("Sad")
