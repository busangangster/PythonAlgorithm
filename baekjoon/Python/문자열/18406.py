import sys
input = sys.stdin.readline

s = input().strip()
t = len(s)//2
first = s[:t]
second = s[t:]
l = 0
r = 0
for x in first:
  l += int(x)
for x in second:
  r += int(x)
if l == r:
  print('LUCKY')
else:
  print("READY")
