import sys
input = sys.stdin.readline

n = int(input())
days = []
ans = []
cnt = 0

for _ in range(n):
  days.append(int(input()))

first = days.pop(0) # 모든 배가 들어오는 날

while len(days) != 0:
  t = days[0] - first
  for i in range(1,days[-1]+1,t): # 배가 들어오는 주기 확인 
    for x in days: # 주기랑 겹치는 배들이 있으면, 그 배들을 리스트에서 제거 
      if x == i:
        days.remove(x)
  cnt +=1  # 주기가 바뀔 때마다 cnt는 1씩 증가 

print(cnt)

  
