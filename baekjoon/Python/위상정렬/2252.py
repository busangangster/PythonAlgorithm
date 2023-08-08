

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)] # 간선에 대한 연결 그래프 초기화
degree = [0] * (n+1) # 각 노드에 대한 진입차수는 0으로 초기화
dq = deque() # 선입선출을 위한 큐 생성

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b) # 노드 a에서 노드 b로 이동
  degree[b] += 1 # b로 진입하는 것이기 때문에 b에 대한 진입차수를 +1 해줌 

for i in range(1,n+1):
  if degree[i] == 0: # 진입차수가 0이면, 출력을 위한 dq에 추가
    dq.append(i)

while dq: # 큐가 비어있을 때까지
  x = dq.popleft()
  print(x,end=' ')
  for i in graph[x]: # 출력한 값과 연결된 노드들의 진입차수를 -1 해줌
    degree[i] -= 1
    if degree[i] == 0: # 해당 노드의 진입차수가 0이 되면 큐에 삽입
      dq.append(i)
    


