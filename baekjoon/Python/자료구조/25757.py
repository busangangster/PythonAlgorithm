import sys
input = sys.stdin.readline
n,g = map(str,input().split())
ans = 0
cnt = 1
dic = {}

for _ in range(int(n)):
  a = input().strip()
  if g == 'Y':
    if a in dic:
      continue
    else:
      dic[a] = 1
      cnt += 1
      if cnt == 2:
        ans += 1
        cnt = 1
  elif g == 'F':
    if a in dic:
      continue
    else:
      dic[a] = 1
      cnt += 1
      if cnt == 3:
        ans += 1
        cnt = 1
  else:
    if a in dic:
      continue
    else:
      dic[a] = 1
      cnt += 1
      if cnt == 4:
        ans += 1
        cnt = 1
print(ans)