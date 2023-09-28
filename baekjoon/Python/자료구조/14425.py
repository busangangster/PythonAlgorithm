import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = []
cnt = 0
for _ in range(n):
  s.append(input().strip())

for i in range(m):
  a = input().strip()
  if a in s:
    cnt += 1
  else:
    continue

print(cnt)