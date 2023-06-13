import sys
input = sys.stdin.readline


n = int(input())
a = 0
b = 1

for _ in range(n-1):
  a,b = b, a+b

print(b)