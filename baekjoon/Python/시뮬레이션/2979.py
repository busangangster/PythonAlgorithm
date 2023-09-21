import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
ans = 0
p = []
for i in range(3):
  f,s = map(int,input().split())
  k = [x for x in range(f,s)]
  p += k

for i in range(1,max(p)+1):
  if p.count(i) == 1:
    ans += a
  elif p.count(i) == 2:
    ans += (b*2)
  elif p.count(i) == 3:
    ans += (c*3)

print(ans)

