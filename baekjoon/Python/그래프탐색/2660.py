import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append([v,0]) # 점수를 체크하기 위해 0을 같이 큐에 추가
  visited[v] = True

  while dq:
    x,y = dq.popleft()

    for i in members[x]:
      if not visited[i]:
        visited[i] = True
        dq.append([i,y+1]) # 큐에 들어갈 때 점수를 1점씩 추가해줌 

  count[v] = y # while문이 종료되었을 때 y가 회원 점수가 됨 

n = int(input())
members = [[] for _ in range(n+1)]
count = [0] * (n+1) # 회원 점수를 기록하는 배열

while True: # 트리 생성 
  a,b = map(int,input().split())
  if a == -1 and b == -1:
    break
  else:
    members[a].append(b)
    members[b].append(a)

for i in range(1,n+1):  #회원 1번부터 점수 몇점인지 BFS로 확인 
  visited = [False] * (n+1)
  BFS(i)

# 결과 출력 과정 
count.pop(0)
ans = []
for i in range(n):
  if count[i] == min(count):
    ans.append(i+1)

print(min(count),count.count(min(count)))
print(*ans)


