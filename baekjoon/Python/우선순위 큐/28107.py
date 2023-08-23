import sys
import heapq as hq
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
orders = [[] for _ in range(200001)]
people = [0] * n

for _ in range(n):
  a = list(map(int,input().split()))
  arr.append(a[1:])

for i in range(n):
  for j in arr[i]:
    hq.heappush(orders[j],i)

b = list(map(int,input().split()))

for i in b:
  if orders[i]:
    people[hq.heappop(orders[i])] += 1
  
print(*people)

