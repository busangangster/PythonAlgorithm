import sys
input = sys.stdin.readline

n = int(input())
chang = 100
sang = 100

for _ in range(n):
  a,b = map(int,input().split())
  if a == b:
    continue
  elif a > b:
    sang -= a
  elif b > a:
    chang -= b

print(chang)
print(sang)