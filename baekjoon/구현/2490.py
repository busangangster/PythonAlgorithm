import sys
input = sys.stdin.readline

for _ in range(3):
  arr = []
  a = list(map(int,input().split()))
  for x in a:
    if x == 0:
      arr.append(x)

  if len(arr) == 1:
    print('A')
  elif len(arr) == 2:
    print('B')
  elif len(arr) == 3:
    print('C')
  elif len(arr) == 4:
    print('D')
  else:
    print('E')