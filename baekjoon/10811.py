import sys

n,m = map(int,sys.stdin.readline().split())
ans = []

for i in range(1,n+1):
  ans.append(i)

for _ in range(m):
  a = list(map(int,sys.stdin.readline().split()))
  ans[a[0]-1:a[1]] = ans[a[0]-1:a[1]][::-1]

for i in ans:
  print(i,end=' ')
