import sys
import heapq as hq
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = []

for i in a: # 선물 상자에 들어있는 선물 수로 최대힙을 만듦
  hq.heappush(arr,-i)

for i in b:
  if i <= -arr[0]: # 최대힙의 루트 노드에 있는 값이 i보다 크거나 같으면
    hq.heappush(arr,-(-hq.heappop(arr) - i)) # 선물주기 가능 
  else: 
    print(0) # 실망하는 경우 
    break

else: # for문이 break 걸리지 않고 끝나면 아이들이 실망하는 경우 X
  print(1)
