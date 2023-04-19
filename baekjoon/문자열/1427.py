import sys

input = sys.stdin.readline

n = int(input())

n = str(n)
ans = []
for i in n:
  ans.append(i)

ans.sort(reverse=True)

for i in ans:
  print(i,end='')
