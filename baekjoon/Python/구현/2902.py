import sys
input = sys.stdin.readline

a = input().strip()
s = a.split('-')
ans = ''
for x in s:
  ans += x[0]

print(ans)