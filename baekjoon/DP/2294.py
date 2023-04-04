

import sys

input = sys.stdin.readline

n,k = map(int,input().split())
dy = [10001] * (k+1) # k의 최댓값이 10,000이므로 dp 배열을 10,001로 초기화
dy[0] = 0

for _ in range(n):
  a = int(input())
  for i in range(a,k+1):
    dy[i] = min(dy[i],dy[i-a]+1) # 최소한의 동전으로 k를 만들 수 있는 방법 찾기
     
if dy[k] == 10001: # dy[k] 값이 10,001이면, k를 동전으로 만들지 못핢
  print(-1)
else: # 만들 수 있으면, dy[k] 출력
  print(dy[k])
  


