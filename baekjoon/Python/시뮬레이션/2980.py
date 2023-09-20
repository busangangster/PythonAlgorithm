import sys
input = sys.stdin.readline

n,l = map(int,input().split())
cur = 0
ans = 0

for _ in range(n):
  d,r,g = map(int,input().split())
  ans += (d - cur)
  cur = d

  if ans % (r + g) <= r:
    ans += (r - (ans%(r+g)))

ans += l - d
print(ans)