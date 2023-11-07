import sys
input = sys.stdin.readline

s,n,m = map(int,input().split())
arr = []
for _ in range(n+m):
  k = int(input())
  if k == 1:
    if len(arr) == s:
      s *= 2
    arr.append(k)
  else:
    arr.pop()

print(s)