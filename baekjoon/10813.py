import sys

n,m = map(int,sys.stdin.readline().split())

ans = []

for i in range(0,n+1):
    ans.append(i)

for _ in range(m):
  a = list(map(int,sys.stdin.readline().split()))
  ans[a[0]],ans[a[1]] = ans[a[1]],ans[a[0]]

for i in range(1,len(ans)):
   print(ans[i],end=' ')  