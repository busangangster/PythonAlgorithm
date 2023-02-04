import sys
import heapq as hq

n = int(sys.stdin.readline())

a = []

for _ in range(n):
  x = int(sys.stdin.readline())
  if x == 0:
    if not a:
      print(0)
    else:
      print(-hq.heappop(a))
  else:
    hq.heappush(a,-x)