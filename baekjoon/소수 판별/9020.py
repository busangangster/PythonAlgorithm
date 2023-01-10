def isPrime(n):
  if n == 1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  else:
    return True

t = int(input())

# 차이가 가장 적은쌍 찾기: 입력받은 값은 반으로 쪼개서 1씩 늘리고 줄여나가면 됨
for _ in range(t):
  n = int(input())
  for j in range(n//2,0,-1): # 두소수의 차이가 가장 적은 쌍을 출력하기 위한 반복문
    if isPrime(j) and isPrime(n-j):
      print(j, n-j)
      break

