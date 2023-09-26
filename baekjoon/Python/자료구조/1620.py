import sys
input = sys.stdin.readline

n,m = map(int,input().split())
poke = {}
num = {}
for i in range(1,n+1):
  p = input().strip()
  poke[p] = i
  num[i] = p

for i in range(m):
  t = input().strip()

  if t.isdigit():
    print(num[int(t)])
  else:
    print(poke[t])
