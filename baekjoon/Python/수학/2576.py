import sys
input = sys.stdin.readline
a = []
hol = []

for _ in range(7):
  a.append(int(input()))

for i in a:
  if i%10 in [1,3,5,7,9]:
    hol.append(i)

if not hol:
  print(-1)
else:
  print(sum(hol))
  print(min(hol))

