import sys
input = sys.stdin.readline

a = input().rstrip()
ans = ''
for x in a:
  t = ord(x) + 13
  if x.isupper():
    if t > 90:
      t = ord(x)-13
    ans += chr(t)
  elif x.islower():
    if t > 122:
      t = ord(x)-13
    ans += chr(t)
  else:
    ans += x
print(ans)