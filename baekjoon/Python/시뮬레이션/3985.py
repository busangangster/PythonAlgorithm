import sys
input = sys.stdin.readline

l = int(input())
n = int(input())
bread = [0] * (l + 1)
bb = []
p = []
cnt = 1

for _ in range(n):
  a,b = map(int,input().split())
  t = 0
  p.append(b-a)
  for i in range(a,b+1):
    if bread[i] == 0:
      bread[i] = cnt
      t += 1
  cnt += 1
  bb.append(t)


for i in range(n):
  if p[i] == max(p):
    print(i+1)
    break

for i in range(n):
  if bb[i] == max(bb):
    print(i+1)
    break