import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans,plus = 0,0
for x in a:
  if x == 1:
    plus += 1
    ans += plus
  else:
    plus = 0

print(ans)