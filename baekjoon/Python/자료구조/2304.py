import sys
input = sys.stdin.readline

n = int(input())
longest = 0
l_idx = 0
s = [0 for _ in range(1001)]

for _ in range(n):
  a,b = map(int,input().split())
  s[a] = b
  if b > longest:
    longest = b
    l_idx = a 

cur = 0
ans = 0

for i in range(l_idx+1):
  cur = max(cur,s[i])
  ans += cur

cur = 0
for i in range(1000,l_idx,-1):
  cur = max(cur,s[i])
  ans += cur

print(ans)