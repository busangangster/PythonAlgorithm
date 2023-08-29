import sys
import heapq as hq
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
order = [[] for _ in range(200001)]
check = [0] * n 

for i in range(n):
  a = list(map(int,input().split()))
  arr.append(a[1:])

b = list(map(int,input().split()))

for i in range(n):
  for j in arr[i]:
    hq.heappush(order[j],i)

for i in b:
  if order[i]:
    check[hq.heappop(order[i])] += 1

print(*check)