import sys
import heapq as hq
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [] # 보석의 가격에 따른 최소힙 
bag = [] # 가방의 무게
j = [] # 보석의 가치를 담을 최대힙

for _ in range(n): # 보석 가격을 기준으로 최소힙을 만들어줌 
  a = list(map(int,input().split()))
  hq.heappush(arr,a)

for _ in range(k):
  bag.append(int(input()))

bag.sort() # 가방의 무게가 오름차순 정렬되어있어야 함 ! 
ans = 0 

for i in bag:
  while arr and arr[0][0] <= i: # 가방에 담을 수 있는 보석의 값어치를 최대힙으로 만들어줌 
    hq.heappush(j,-hq.heappop(arr)[1])
  
  if j: # j가 비어있을 경우 pop을 못하기 때문에 조건문이 있어야 함 ! 
    ans += -hq.heappop(j)

print(ans)

    