import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a = sorted(list(map(int,input().split())))
  t = a[1:-1]
  if t[-1] - t[0] >= 4:
    print('KIN')
  else:
    print(sum(t))