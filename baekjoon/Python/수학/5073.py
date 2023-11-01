import sys
input = sys.stdin.readline

while True:
  a = list(map(int,input().split()))
  if all(x for x in a) == 0:
    break
  else:
    a.sort()
    if a[-1] >=  a[0] + a[1]:
      print('Invalid')
    else:
      if a[0] == a[1] == a[2]:
        print('Equilateral')
      elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        print('Isosceles')
      else:
        print('Scalene')