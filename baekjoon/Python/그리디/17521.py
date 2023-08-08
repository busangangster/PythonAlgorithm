import sys
input = sys.stdin.readline

n,w = map(int,input().split())
coins = []
coin = 0

for _ in range(n):
  coins.append(int(input()))

for i in range(n-1):
  if coins[i] < coins[i+1]: # 매수
    if w // coins[i] > 0:
      coin = w // coins[i]
      w = w % coins[i]
  elif coins[i] > coins[i-1]: # 매도 
    w += (coin * coins[i])
    coin = 0 

if coin != 0: # 코인이 남아있으면 마지막 날에 전부 매도 
  w += coin * coins[-1]

print(w)
  