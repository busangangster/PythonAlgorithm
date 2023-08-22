import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  a = list(map(int,input().split()))
  if a[0] == 0:
    if arr:
      print(arr)
      print(-hq.heappop(arr)) # 출력할 때는 양수로 출력하기 위해 - 부호 붙여서 출력
    else:
      print(-1) # 힙이 비어있으면 -1 출력 
  else:
    for i in range(1,a[0]+1): # 힙에 선물 넣기 
      hq.heappush(arr,-a[i]) # 최대힙으로 만들기 위해 부호를 반대로 삽입