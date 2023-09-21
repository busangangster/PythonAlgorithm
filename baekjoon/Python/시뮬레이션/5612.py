import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
tunnel = []
tunnel.append(m)
cur = m

for _ in range(n):
  a,b = map(int,input().split())
  cur += a
  cur -= b
  tunnel.append(cur)

if min(tunnel) < 0:
  print(0)
else:
  print(max(tunnel))