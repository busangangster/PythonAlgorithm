import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def DFS():
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(n):
      ans.append(a[i])
      DFS()
      ans.pop()

DFS()