import sys
input = sys.stdin.readline

a = list(map(int,input().split()))
b = sorted(a)

while a != b:
  for i in range(4):
    if a[i] > a[i+1]:
      a[i],a[i+1] = a[i+1],a[i]
      print(*a)
