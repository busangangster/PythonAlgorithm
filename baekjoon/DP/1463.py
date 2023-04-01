
import sys

n = int(sys.stdin.readline())
dy = [0] * (n+1) # 최소 연산 횟수를 저장할 DP 리스트 생성 

for i in range(2,n+1): # dy[1] == 0이기 때문에 2부터 n까지 반복문 실행
  dy[i] = dy[i-1] + 1 # 기본 최소 연산 횟수

  if i%2 == 0: # 2로 나누어 떨어졌을 때
    dy[i] = min(dy[i],dy[i//2]+1) # 최소값 선택

  if i%3 == 0: # 3으로 나눠 떨어졌을 때
    dy[i] = min(dy[i],dy[i//3]+1) # 최소값 선택

print(dy[n])


