import sys
input = sys.stdin.readline

n = int(input())
a,b,c = map(int,input().split())
ans = 0
for x in [a,b,c]:
  if x > n:
    ans += n
  else:
    ans += x
print(ans)