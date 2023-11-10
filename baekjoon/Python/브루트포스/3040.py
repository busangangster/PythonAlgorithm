import sys
input = sys.stdin.readline

s = []
for _ in range(9):
  s.append(int(input()))

for i in range(9):
  for j in range(i+1,9):
    if sum(s) - (s[i] + s[j]) == 100:
      t = s[i]
      k  = s[j]
      break

s.remove(t)
s.remove(k)
for x in s:
  print(x)