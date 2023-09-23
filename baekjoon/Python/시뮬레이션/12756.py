import sys
input = sys.stdin.readline

a = list(map(int,input().split()))
b = list(map(int,input().split()))

while True:
  if a[1] <= 0 or b[1] <= 0:
    break
  else:
    a[1] = a[1] - b[0]
    b[1] = b[1] - a[0]

if a[1] <= 0 and b[1] <= 0:
  print('DRAW')
elif a[1] > b[1]:
  print('PLAYER A')
elif a[1] < b[1]:
  print('PLAYER B')