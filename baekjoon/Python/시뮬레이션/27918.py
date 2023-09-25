import sys
input = sys.stdin.readline

n = int(input())
d = 0
p = 0
w = []
for _ in range(n):
  w.append(input().strip())
  
for x in w:
  if d >= p + 2 or p >= d + 2:
    break
  else:
    if x == 'D':
      d += 1
    else:
      p += 1

print(d,':',p,sep='')
