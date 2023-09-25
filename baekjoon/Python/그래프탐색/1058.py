import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
  a = list(input().strip())
  for j in range(len(a)):
    if a[j] == 'Y':
      graph[i].append(j+1)
      graph[j+1].append(i)
    else:
      continue

print(graph)

