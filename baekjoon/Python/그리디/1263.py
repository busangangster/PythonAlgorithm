

import sys
input = sys.stdin.readline

n = int(input())
tasks = []

for _ in range(n):
  a,b = map(int,input().split())
  tasks.append([a,b])

tasks.sort(key = lambda x:x[1]) # 람다 표현식으로 b를 기준으로 오름차순 정렬

start = 0 # 진영이가 일을 시작하는 시각
flag = True # while문을 빠져나오기 위한 변수

while True:
  time = start 
  for i in range(len(tasks)):
    # 일을 주어진 시간 안에 끝낼 수 있는 경우
    if time + tasks[i][0] <= tasks[i][1]:
      time += tasks[i][0]
    else:
      # 아닌 경우는 flag를 False로 바꾸고 반복문 탈출
      flag = False
      break
  else: # for문이 break에 걸리지 않으면, 일을 시작하는 시각에 +1을 해줌 
    start += 1

  if flag == False: # for문이 끝났을 때 flag가 False면 while문 종료
    break

# start에 -1을 하는 이유는 풀이 참고 ! 
if start-1 == 0:
  print(-1)
else:
  print(start-1)









