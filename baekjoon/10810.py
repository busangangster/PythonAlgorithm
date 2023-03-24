import sys
n,m = map(int,sys.stdin.readline().split())
ans = [0] * (n+1)

for _ in range(m):
  a = list(map(int,sys.stdin.readline().split()))
  for i in range(a[0],a[1]+1):
    ans[i] = a[2]

for i in range(1,len(ans)):
  print(ans[i],end=' ')




