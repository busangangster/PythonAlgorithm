
import sys
import heapq as hq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  max_arr = [] # 최대힙
  min_arr = [] # 최소힙 
  k = int(input())
  for _ in range(k):
    a,b = map(str,input().split())
    
    if not max_arr and min_arr and a == 'D':
      continue
    else:

      if a == 'I':
        hq.heappush(max_arr,-int(b))
        hq.heappush(min_arr,int(b))

      elif a == 'D' and b == '1':
        hq.heappop(max_arr)
      
      elif a == 'D' and b == '-1':
        hq.heappop(min_arr)
    print(max_arr)
    print(min_arr)

  if max_arr and min_arr:
    print(-max_arr[0],min_arr[0])
  else:
    print('EMPTY')

