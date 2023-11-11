import sys
input = sys.stdin.readline

n = int(input())
for _ in range(9):
  a = int(input())
  n -= a
print(n)