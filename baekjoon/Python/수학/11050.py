import sys
input = sys.stdin.readline

n,k = map(int,input().split())
up = 1
cnt = 0

for i in range(n,0,-1):
  if cnt == k:
    break
  else:
    up *= i 
    cnt += 1

down = 1
count = 0

for i in range(k,0,-1):
  if count == k:
    break
  else:
    down *= i
    count += 1

print(up//down)