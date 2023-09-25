import sys
from collections import deque
input = sys.stdin.readline

w = [[0]]
score = [0,1,2,4,8]
ans = 0
for _ in range(4):
  w.append(list(input().strip()))

k = int(input())
for _ in range(k):
  num,d = map(int,input().split())

  direction = [0] * 5
  direction[num] = d

  l,r = num - 1, num
  while l > 0:
    if w[l][2] != w[r][6]:
      direction[l] = direction[r] * -1

    else:
      break
    l,r = l-1, r-1

  l,r = num, num + 1
  while r < 5:
    if  w[l][2] != w[r][6]:
      direction[r] = direction[l] * -1
    else:
      break
    l,r = l+1, r+1

  for i in range(1,5):
    if direction[i] == 1:
      w[i].insert(0,w[i].pop())
    elif direction[i] == -1:
      w[i].append(w[i].pop(0))

for i in range(1,5):
  if w[i][0] == '1':
    ans += score[i]

print(ans)