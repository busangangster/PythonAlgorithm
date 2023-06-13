import sys
input = sys.stdin.readline

while True:
  a = list(map(int,input().split()))
  if a == [0,0,0]:
    break
  else:
    a.sort()
    if a[-1]**2 == a[0]**2 + a[1]**2:
      print('right')
    else:
      print('wrong')



