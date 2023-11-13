import sys
input = sys.stdin.readline

ans = 0
max_v = -2147000000
for _ in range(4):
  a,b = map(int,input().split())
  ans += (b-a)
  max_v = max(ans,max_v)

print(max_v)