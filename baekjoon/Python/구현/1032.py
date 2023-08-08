import sys
input = sys.stdin.readline

n = int(input())
a = list(input())

for _ in range(n-1):
  b = list(input())
  for i in range(len(a)):
    if a[i] != b[i]:
      a[i] = '?'

for x in a:
  print(x,end='')

