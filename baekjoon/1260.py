from sys import stdin

n, e, m = map(int,stdin.readline().split())
N = [[0]*(n+1) for _ in range(n+1)]

#print(N)

for _ in range(e):
    line = list(map(int, stdin.readline().split()))
    #N[line[0]][line[1]] = 1
    #N[line[1]][line[0]] = 1

print(line)



'''
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
'''
