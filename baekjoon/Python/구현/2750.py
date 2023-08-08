import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
  a = int(input())
  ans.append(a)

ans.sort()

for x in ans:
  print(x)