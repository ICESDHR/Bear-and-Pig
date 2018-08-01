# -*- coding:utf-8 -*-

# 机器人的运动范围
# TODO 自己想了好久没想出来，写的是错的
def movingCount(threshold, rows, cols):
    ans = []
    moving(threshold, rows, cols, 0, 0, ans)
    return len(ans)

def moving(threshold, rows, cols, col, row, ans):
    if sum(map(int, list(str(col)))) + sum(map(int, list(str(row)))) <= threshold and (col, row) not in ans:
        ans.append((col, row))
        if col+1 < cols:
            moving(threshold, rows, cols, col+1, row, ans)
        if row+1 < rows:
            moving(threshold, rows, cols, col, row+1, ans)
    return


def MovingCount(threshold, rows, cols):
    count = 0
    x1,y1 = int(rows/10),int(cols/10)
    x2,y2 = rows%10,cols%10
    if x1 + y1 <= threshold-18:
        return rows*cols
    for i in range(x1,-1,-1):
        for j in range(y1,-1,-1):
            key = threshold-i-j
            if key < 0:
                break
            elif key >= 18:
                if i+j <= x1+y1-2:
                    count = count+10*10
                elif i == x1-1:
                    count = count+10*(cols-10*j+1)
                else:
                    count = count+10*(rows-10*i+1)
                break
            else:
                for k in range(min(9,key,rows-10*i)+1):
                    count = count + min((key-k+1),(cols-10*j+1))
    return count


if __name__ == '__main__':
    threshold = 18
    rows,cols = 50,50
    print(movingCount(threshold, rows, cols))
