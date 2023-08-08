import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cus = []

for _ in range(m):
  cus.append(int(input()))

cus.sort(reverse = True)
max = 0 # 최대 수익
price = 0 # 책정한 가격

for i in range(min(n,m)):
  p = cus[i] # 최대 이익을 측정하기 위한 가격 설정 
  num = 0 # 몇개의 달걀을 팔 수 있는지
  for j in range(min(n,m)):
    # 고객의 구매의사 가격이 설정가보다 높으면 달걀 팔 수 있음
    if cus[j] >= p: 
      num += 1
    else:  # 내림차순 정렬했기 때문에 else문에 걸리면 그 다음 요소들도 조건문을 반족 X 
      break  # 반복문 바로 빠져나옴

  # 이중 반복문이 끝났을 때 책정 가격과 이익을 변수에 저장 
  if p * num > max:
    max = p*num
    price = p

print(price,max)
