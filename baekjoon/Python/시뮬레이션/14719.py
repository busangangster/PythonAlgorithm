import sys
input = sys.stdin.readline

h,w = map(int,input().split())
a = list(map(int,input().split()))
ans = 0

for i in range(1,w-1):
  l_max = max(a[:i])
  r_max = max(a[i+1:])

  t = min(l_max,r_max)

  if a[i] < t:
    ans += t - a[i]

print(ans)