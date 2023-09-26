import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
red = 0
blue = 0
cnt = 0
ans = []

for i in range(n):
  if a[i] == 'R':
    red += 1
  
  elif a[i] == 'B' and red:
    cnt += red
    red = 0
ans.append(cnt)
cnt = 0

for i in range(n):
  if a[i] == 'B':
    blue += 1
  elif a[i] == 'R' and blue:
    cnt += blue
    blue = 0
ans.append(cnt)
cnt = 0

a.reverse()
red = 0
blue = 0

for i in range(n):
  if a[i] == 'R':
    red += 1
  elif a[i] == 'B' and red:
    cnt += red
    red = 0
ans.append(cnt)
cnt = 0

for i in range(n):
  if a[i] == 'B':
    blue += 1
  elif a[i] == 'R' and blue:
    cnt += blue
    blue = 0
ans.append(cnt)

print(min(ans))