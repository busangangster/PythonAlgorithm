import sys
input = sys.stdin.readline

s = 'CAMBRIDGE'

a = input().strip()
ans =''

for i in a:
  if i in s:
    continue
  else:
    ans += i

print(ans)
