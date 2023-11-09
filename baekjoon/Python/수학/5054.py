import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  a = sorted(list(map(int,input().split())))
  min_v = 2147000000
  for i in range(n):
    d = ((a[i] - a[0]) * 2) + ((a[-1] - a[i]) *2)
    if d < min_v:
      min_v = d
  print(min_v)