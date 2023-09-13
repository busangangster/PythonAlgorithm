import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def DFS(start):
  overlap = 0
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(start,n):
      if overlap != a[i]:
        ans.append(a[i])
        overlap = a[i]
        DFS(i)
        ans.pop()

DFS(0)
