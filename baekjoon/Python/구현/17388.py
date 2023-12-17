import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

ans = a+b+c
if ans >= 100:
  print('OK')
else:
  k = min(a,b,c)
  if k == a:
    print('Soongsil')
  elif k == b:
    print('Korea')
  else:
    print('Hanyang')