import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []
check = [False] * n

def DFS(start):
  overlap = 0
  if len(ans) == m:
    print(*ans)
    return
  else:
    for i in range(start,n):
      if check[i] == False and overlap != a[i]:
        ans.append(a[i])
        check[i] = True
        overlap = a[i]
        DFS(i+1)
        ans.pop()
        check[i] = False

DFS(0)
