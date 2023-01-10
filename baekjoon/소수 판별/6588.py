n = 1000000
a = [0] * (n+1)


for i in range(2,int(n**0.5)+1):
  if a[i] == 0:
    # J를 도는 for문이 i로 시작하면, 소수도 전부 1로 변환됨 
    for j in range(i+i,n+1,i): # i+i로 시작하면, 소수는 빼고 세아릴수 있다
      a[j] = 1

while True:
  k = int(input())
  if  k == 0:
    break
  for i in range(2,n//2+1):
    if a[i]==0 and a[k-i]==0: # 소수 판별
      print(k,"=",i,"+",k-i)
      break
  else:
    print("Goldbach's conjecture is wrong.")

