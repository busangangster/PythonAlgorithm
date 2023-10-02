
import sys
import heapq as hq
input = sys.stdin.readline

n,h,t = map(int,input().split())
arr = []
cnt = 0
for _ in range(n): # 최대힙으로 만들기 위해 음수로 append 
  arr.append(-int(input()))

hq.heapify(arr)

while arr and cnt != t:
  if -arr[0] >= h: # 거인들의 키가 더 크거나 같을 때
    if -arr[0] == 1: # 최대힙인데 1이 나오면 while문 바로 종료
      break
    else: # 거인의 키를 1/2로 줄여나가고, cnt를 1씩 증가 
      hq.heappush(arr,int((hq.heappop(arr)/2)))
      cnt += 1
  else:
    break

if all(h > -x for x in arr): # while문이 끝났을 때 arr안의 모든 원소가 h보다 작으면 yes
  print('YES')
  print(cnt)
  
else: # 아니면 NO 
  print('NO')
  print(-arr[0])


  



