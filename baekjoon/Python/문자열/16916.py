import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

if b in a:
  print(1)
else:
  print(0)