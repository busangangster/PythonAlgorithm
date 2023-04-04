

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a = a[::-1]
a.insert(0,0)

dy = [0] * (n+1)

for i in range(1,n+1):
  length = 0
  for j in range(i-1,0,-1):
    if a[i] > a[j] and dy[j] > length:
      length = dy[j]
  dy[i] = length + 1

print(max(dy))

