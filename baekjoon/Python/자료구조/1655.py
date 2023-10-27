import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
left = [] # 최대힙
right = [] # 최소힙 

for _ in range(n):
  a = int(input())

  if len(left) == len(right):
    hq.heappush(left,-a) # 최대힙으로 만들기 위해 '-'부호로 push
  else:
    hq.heappush(right,a) # 최소힙
  
  if right and -left[0] > right[0]: # 최대힙의 가장 작은 수가 최소힙의 가장 작은 수보다 크면
    hq.heappush(right,-hq.heappop(left)) # 둘이 교환
    hq.heappush(left,-hq.heappop(right))

  print(-left[0]) # 최대힙의 첫번째 요소를 출력 

