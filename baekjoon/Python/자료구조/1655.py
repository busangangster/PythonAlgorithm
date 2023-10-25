import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
lt_heap = []
rt_heap = []

for _ in range(n):
  a = int(input())
  
  if len(lt_heap) == len(rt_heap):
    hq.heappush(lt_heap,-a)
  else:
    hq.heappush(rt_heap,a)
  
  if rt_heap and -lt_heap[0] > rt_heap[0]:
    lt = -hq.heappop(lt_heap)
    rt = hq.heappop(rt_heap)

    hq.heappush(lt_heap,-rt)
    hq.heappush(rt_heap,lt)

  print(-lt_heap[0])
  