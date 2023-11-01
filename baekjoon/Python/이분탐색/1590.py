import sys
input = sys.stdin.readline

n,t = map(int,input().split())
ans = []
for _ in range(n):
  cnt = 0
  s,i,c = map(int,input().split())
  bus = [s]
  k = s
  for x in range(c-1): # 버스 배차 간격을 리스트로 만듦 
    k += i 
    bus.append(k)
  lt = 0
  rt = c-1

  while lt <= rt: # 이분탐색 시작 
    mid = (lt+rt) // 2

    if bus[mid] >= t:
      cnt = bus[mid]
      rt = mid - 1
    else:
      lt = mid + 1

  if cnt == 0: # 출발할 수 있는 값이 없으면 continue
    continue
  else:
    ans.append(cnt-t) # 있다면, 버스 출발시간에서 영식이 도착시간 빼주기

if not ans: # 탈 수 있는 버스가 없으면 -1 출력
  print(-1)
else:
  print(min(ans)) # 버스를 타기 위해 최소한으로 기다리는 시간 출력
