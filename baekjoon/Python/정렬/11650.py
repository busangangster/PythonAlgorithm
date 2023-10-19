import sys
input = sys.stdin.readline
n = int(input())
ans = []
for _ in range(n):
  a,b = map(int,input().split())
  ans.append([a,b])

ans.sort(key = lambda x:(x[0],x[1]))

for a,b in ans:
  print(a,b)