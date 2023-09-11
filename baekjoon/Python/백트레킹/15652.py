import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []

def DFS(start):
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(start,n+1):
      ans.append(i)
      DFS(i)
      ans.pop()

DFS(1)
