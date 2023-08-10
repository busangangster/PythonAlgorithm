import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  stock = list(map(int,input().split()))
  max = 0
  sum = 0

  for i in range(n-1,-1,-1): # 주식 가격 뒤에서부터 접근
    if stock[i] > max: # 해당 가격이 max값보다 크면 
      max = stock[i] # max 변경
    else:
      sum += max - stock[i] # 아니면 이익에 차익을 더해줌 

  print(sum)

