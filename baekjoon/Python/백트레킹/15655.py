import sys
input = sys.stdin.readline

n,m= map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def DFS(start):
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(start,n):
      if a[i] not in ans:
        ans.append(a[i])
        DFS(i)
        ans.pop()

DFS(0)