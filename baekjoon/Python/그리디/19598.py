import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
arr = []
t = []
cnt = 0
for _ in range(n):
  arr.append(list(map(int,input().split())))

arr.sort()

for i in arr:
  if t and t[0] <= i[0]:
    hq.heappop(t)
    hq.heappush(t,i[1])
  else:
    hq.heappush(t,i[1])

print(len(t))