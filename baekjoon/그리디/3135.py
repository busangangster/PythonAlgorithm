import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n = int(input())
hz = []
ans = abs(a-b) # 초기값을 a - b의 절대값으로 설정

for _ in range(n):
  hz.append(int(input()))

if b in hz: # 리스트 안에 b 값이 있으면 바로 이동 가능하므로 1 출력 
  print(1)
else:
  for x in hz: # 리스트 안에 있는 값들을 하나씩 비교하면서 최소값을 ans로 설정
    ans = min(ans, abs(x-b)+1)
  print(ans)
  

