import sys
from collections import deque
input = sys.stdin.readline

move = [1,2,3,4,5,6] # 주사위를 던져서 이동할 수 있는 경우 

def BFS(v):
  dq = deque()
  dq.append([v,0]) # 현재 위치와, 주사위를 몇번 던졌는지 확인해주기 위한 0
  visited[v] = True

  while dq:
    x,y = dq.popleft()

    if x == 100: # 위치가 100이되면 횟수 출력한 뒤 종료 
      print(y)
      sys.exit()

    for i in range(6):
      xx = x + move[i]

      if 0 < xx <= 100 and not visited[xx]:
        for k in ladder: # 만약 위치가 사다리 or 뱀을 이용할 수 있다면 
          if xx == k[0]:
            xx = k[1] # 그 위치로 이동 
        visited[xx] = True
        dq.append([xx,y+1])

n,m = map(int,input().split())
ladder = []
for _ in range(n+m): # 사다리 + 뱀으로 이동할 수 있는 경우를 ladder에 넣음
  a,b = map(int,input().split())
  ladder.append([a,b])

visited = [False] * (101)
BFS(1)