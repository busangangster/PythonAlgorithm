import sys

n = int(sys.stdin.readline())

for _ in range(n):
  a = int(sys.stdin.readline())
  dy = [0] * (a+1)
  if a == 1:
    print(1)
  elif a == 2:
    print(2)
  elif a == 3:
    print(4)
  else:
    dy[1] = 1
    dy[2] = 2
    dy[3] = 4
    for i in range(4,a+1):
      dy[i] = dy[i-1] + dy[i-2] + dy[i-3]

    print(dy[a])
