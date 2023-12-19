import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
check = []
cnt = 0
enter = deque(input().strip() for _ in range(n))
out = deque(input().strip() for _ in range(n))

while out:
  if enter[0] in check:
    enter.popleft()
  else:
    k = out.popleft()
    if k != enter[0]:
      cnt += 1
      check.append(k)
    else:
      enter.popleft()
      
print(cnt)
