

import sys
t = int(sys.stdin.readline())

for _ in range(t):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  dy = [i for i in range(1,n+1)] # 0층에 거주하는 사람
  
  for i in range(k): # 층 수만큼 반복
    for j in range(1,n): # 1호부터 n호까지 
      # n+1이 아니라 n까지 범위를 설정하는 이유는 인덱스 특성 때문 ! 

      dy[j] += dy[j-1] # 누적 시키기 

  print(dy[-1])

