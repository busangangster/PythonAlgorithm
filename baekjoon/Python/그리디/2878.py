# 문제의 핵심 : 모자란 사탕을 최대한 균등하게 나눠줘야 분노의 합이 최소 ! 


import sys
input = sys.stdin.readline

m,n = map(int,input().split())
candy = []
res = 0

for _ in range(n):
  candy.append(int(input()))

candy.sort() # 균등하게 나누기 위해 오름차순으로 작은 수부터 시작 
need = sum(candy) - m # 모자란 사탕의 수 

for i in range(n):
  # 원래 받으려고 했던 사탕보다 더 받을 수는 없기 때문에 둘의 최솟겂을 선택
  tmp = min(candy[i],need // (n-i)) 
  res += tmp**2
  need -= tmp

print(res % 2**64)

   