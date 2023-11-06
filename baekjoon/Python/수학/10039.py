import sys
input = sys.stdin.readline
s = []
for _ in range(5):
  a = int(input())
  if a >= 40:
    s.append(a)
  else:
    s.append(40)
print(sum(s)//len(s))
