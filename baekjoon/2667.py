#DFS 풀이법

import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            # 범위 check
            if matrix[n_x][n_y]==1:
            # 그부분이 1이면
                cnt = dfs(matrix, cnt+1, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인
    return cnt
    # 다 cnt검사하면 끝을 낸다.

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)


#BFS 풀이법

import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(matrix, cnt, x, y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 그래서 0으로 바꾼다
    queue = []
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.pop()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if matrix[nx][ny] == 1:
                    cnt += 1
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(bfs(matrix, cnt+1, i, j))
            # 여기서 이제 그 주위에 있는 것들 다 돌아보는것이다.
print(len(ans))
for i in sorted(ans):
    print(i)