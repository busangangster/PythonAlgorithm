import sys
input = sys.stdin.readline

a = list(input().strip().split('-'))
n = int(input())
f = int(a[0])
s = int(a[1])
l = int(a[-1])

l = l + n
if l > 30:
  if l % 30 == 0:
    s += l // 30 -1
    l = 30
  else:
    s += l // 30
    l = l % 30

  if s > 12:
    if s %  12 == 0:
      f += s // 12 - 1
      s = 12
    else:
      f += s // 12
      s = s % 12

if s < 10:
  if l < 10:
    print('{}-0{}-0{}'.format(f,s,l))
    sys.exit()
  else:
    print('{}-0{}-{}'.format(f,s,l))
elif l < 10:
  print('{}-{}-0{}'.format(f,s,l))
else:
  print('{}-{}-{}'.format(f,s,l))
