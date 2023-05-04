

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  a = list(input().strip().split(' '))
  for i in range(len(a)):
    a[i] = a[i][::-1]
  for x in  a:
    print(x,end=' ')
  print()


