import sys
input = sys.stdin.readline

n,m = map(int,input().split())
sets = []
one = []
for _ in range(m):
  s,d = map(int,input().split())
  sets.append(s)
  one.append(d)

a = min(sets) # 세트 가격 중 최솟값
b = min(one) # 낱개 가격 중 최솟값 

k = n // 6
t = n % 6
sum = 0

# 세트 가격이 낱개 가격으로 6개 사는 것보다 비쌀경우
# 낱개로 사는 게 더 싸니까 낱개로 n개 전부 구매 
if a > b*6:
  sum += n*b
# 아닐 경우 
else:
  sum += k*a # sum에 n을 6으로 나눈 몫과 a의 곱을 더해줌
  if t*b < a: # 만약 n을 6으로 나눈 나머지와 낱개의 가격이 세트 가격보다 낮으면
    sum += t*b # sum에 낱개 가격으로 추가
  else: # 아니면 세트로 사는 게 더 쌈
    sum += a
  
print(sum)

