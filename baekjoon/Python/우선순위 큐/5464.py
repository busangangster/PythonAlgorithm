import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
fine = []
weight = []
lot = [0] * n
wait = deque()
fee = 0

for _ in range(n):
  fine.append(int(input()))

for _ in range(m):
  weight.append(int(input()))

for _ in range(2*m):
  car = int(input().strip())
  if car > 0 :
    if 0 in lot:
      for i in range(n):
        if lot[i] == 0:
          lot[i] = car
          break
    else:
      wait.append(car)
  else:
    t = lot.index(-car)
    lot[t] = 0
    fee += fine[t] * weight[-car-1]
    if wait:
      lot[t] = wait.popleft()

print(fee)
