import sys
n = sys.stdin.readline().strip()
res = ''

a = sorted(n,reverse= True)

for x in a :
  res += x

if int(res)% 30 != 0:
  print(-1)
else:
  print(res)