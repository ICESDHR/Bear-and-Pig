graph = [[-1 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    i, j = map(int, input().strip().split(" "))
    print(i, j)
    graph[i][j] = 1
    graph[j][i] = 1


line = sys.stdin.readline().strip()
n, k = list(map(float, line.split()))