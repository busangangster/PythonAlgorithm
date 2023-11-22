import sys
import heapq as hq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  q = []
  ans = 0
  for x in a:
    hq.heappush(q,x)
  print(q)

  while len(q) != 1:
    first = hq.heappop(q)
    second = hq.heappop(q)
    result = first + second
    ans += result
    hq.heappush(q,result)
  print(ans)
