import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a = list(input().split())
  n = float(a[0])
  for i in range(1,len(a)):
    if a[i] == '@':
      n *= 3
    elif a[i] == '%':
      n += 5
    elif a[i] == '#':
      n -= 7

  print('{:.2f}'.format(n))