import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a = input().strip()
  s = a[0].upper() + a[1:]
  print(s)