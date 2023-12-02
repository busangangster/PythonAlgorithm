import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = str(n)*n

if len(s) >= m:
  print(s[:m])
else:
  print(s)