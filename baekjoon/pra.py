import sys
import heapq as hq
input = sys.stdin.readline

a = [2,1,1,4,3,4]
# hq.heapify(a)
print(a)
b = []
for x in a:
  hq.heappush(b,x)
print(b)
