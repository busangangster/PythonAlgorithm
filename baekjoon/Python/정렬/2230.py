import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
for _ in range(n):
  a.append(int(input()))
a.sort()
lt = 0
rt = 0
ans = 2147000000

while lt < n and rt < n:
  mid = a[rt] - a[lt]

  if mid >= m:
    ans = min(ans,mid)
    lt += 1
  
  else:
    rt += 1
print(ans)