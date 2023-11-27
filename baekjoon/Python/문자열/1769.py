import sys
input = sys.stdin.readline

s = input().strip()
ans = 0
cnt = 0
while len(s) != 1:
  for x in s:
    ans += int(x)
  s = str(ans)
  ans = 0
  cnt += 1

if s in ['3','6','9']:
  print(cnt)
  print('YES')
else:
  print(cnt)
  print('NO')