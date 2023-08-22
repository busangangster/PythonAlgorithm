import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
  a = list(map(int,input().split()))
  for j in a:
    if len(ans) < n:
      hq.heappush(ans,j)
    else:
      if j > ans[0]:
        hq.heappop(ans)
        hq.heappush(ans,j)

print(ans[0])