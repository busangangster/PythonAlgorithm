import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
arr = []
t = []
for _ in range(n):
  arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[1])

for i in arr:
  if t and t[0] <= i[1]:
    hq.heappop(t)
    hq.heappush(t,i[2])
  else:
    hq.heappush(t,i[2])

print(len(t))