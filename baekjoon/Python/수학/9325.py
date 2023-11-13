import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
  p = int(input())
  ans = p
  n = int(input())
  for _ in range(n):
    a,b = map(int,input().split())
    ans += a*b
  
  print(ans)