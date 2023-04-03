

import sys 

n = int(sys.stdin.readline())

for _ in range(n):
  a = int(sys.stdin.readline())
  dy = [[0 for _ in range(2)] for _ in range(a+1)]

  if a == 0:
    print(1,0)
  elif a == 1:
    print(0,1)
  else:
    dy[0] = [1,0]
    dy[1] = [0,1]
    for i in range(2,a+1):
      dy[i][0] = dy[i-2][0] + dy[i-1][0]
      dy[i][1] = dy[i-2][1] + dy[i-1][1]
    print(dy[a][0],dy[a][1])


