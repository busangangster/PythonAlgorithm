import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
A,B = map(int,input().split())
m = int(input())
check = [False] * (n+1)
arr = [[] for _ in range(n+1)]
ans = [0] * (n+1)

for _ in range(m): # 인접노드 탐색과정 
  x,y = map(int,input().split())
  arr[x].append(y)
  arr[y].append(x)

# arr = [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

def DFS(v): # 인접노드를 방문하면서 촌수를 찾아가는 과정 
  check[v] = True
  for i in arr[v]:
    if not check[i]:
      ans[i] = ans[v] + 1
      DFS(i)

DFS(A) # 시작점 = 자식노드 
      
if ans[B] == 0 : 
  print(-1)
else:
  print(ans[B])
