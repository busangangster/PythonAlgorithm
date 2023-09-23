import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(k):
  a,b = map(int,sys.stdin.readline().split())
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

# bfs
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# k = int(input())
# graph = [[] for _ in range(n+1)]
# cnt = 0

# for _ in range(k):
#   a,b = map(int,input().split())
#   graph[a].append(b)
#   graph[b].append(a)


# def BFS(graph,v,visited):
#   global cnt
#   visited[v] = True
#   dq = deque()
#   dq.append(v)

#   while dq:
#     f = dq.popleft()

#     for i in graph[f]:
#       if not visited[i]:
#         visited[i] = True
#         dq.append(i)
#     cnt += 1
#   return cnt-1

# visited = [False] * (n+1)
# print(BFS(graph,1,visited))