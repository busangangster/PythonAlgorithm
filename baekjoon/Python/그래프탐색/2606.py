import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(k):
  a,b = map(int,sys.stdin.readline().split())
  # 각각의 컴퓨터를 서로 연결 시킴
  graph[a] += [b]
  graph[b] += [a]

def DFS(x):
  global cnt
  visited[x] = 1
  for i in graph[x]:
    if visited[i] == 0:
      DFS(i) # 선택한 경로로 이어진 간선들의 수만큼 DFS 반복
      cnt += 1

DFS(1)
print(cnt)
