import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [0] * (n+1)
arr.insert(0,0) # 인덱스 1부터 시작하기 위해 0을 추가해줌 

# 구매하려는 카드의 개수가 하나일 때부터 시작 
for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i],dp[i-j] + arr[j])

print(dp[n])
