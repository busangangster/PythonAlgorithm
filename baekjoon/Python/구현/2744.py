import sys
input = sys.stdin.readline

a = list(input().strip())
s = ''

for x in a:
  if x.islower():
    s += x.upper()
  else:
    s += x.lower()
print(s)
    