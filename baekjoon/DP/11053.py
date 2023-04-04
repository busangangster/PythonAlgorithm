
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.insert(0,0) # 리스트 a의 인덱스를 1부터 생각하기 위해 '0' 삽입

dy = [0] * (n+1)

for i in range(1,n+1):
  length = 0 # 부분 수열의 길이

  for j in range(i-1,0,-1):
    # 수열 a의 마지막 숫자가 그 전 숫자보다 크며, 부분 수열의 길이가 기존보다 더 클 때
    if a[j] < a[i] and dy[j] > length: 
      length = dy[j] 

  dy[i] = length + 1 # 가장 긴 부분 수열에 +1 

print(max(dy))




