import sys
import heapq as hq
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
arr = []
ans = 0

a.sort(reverse= True)

for i in a:
  if len(arr) < m:
    hq.heappush(arr,i)
  else:
    hq.heappush(arr,hq.heappop(arr) + i)

print(max(arr))