import sys
input = sys.stdin.readline

s = list(input().strip().split(','))
ans = 0
for x in s:
  ans += int(x)

print(ans)