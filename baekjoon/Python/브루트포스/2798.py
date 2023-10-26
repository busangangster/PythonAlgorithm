import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
arr = []
ans = -2147000000
arr = list(combinations(a,3))

for x in arr:
  if sum(x) <= m:
    ans = max(ans,sum(x))

print(ans)

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      cur = a[i]+a[j]+a[k]
      if cur <= m:
        ans = max(ans,cur)

print(ans)