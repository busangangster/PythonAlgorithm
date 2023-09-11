import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def DFS():
  overlap = 0
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(n):
      if overlap != a[i]:
        ans.append(a[i])
        overlap = a[i]
        DFS()
        ans.pop()

DFS()
