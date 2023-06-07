

import sys
from collections import deque
input = sys.stdin.readline
dia = []
w = []

n,k = map(int,input().split())
for _ in range(n):
  dia.append(list(map(int,input().split())))
  
for _ in range(k):
  w.append(int(input()))

dia.sort(reverse = True)
w.sort(reverse = True)
dq  = deque(dia)

print(dq,w)

# for x in dq:
#   if x[0] <= w[0]

  

    