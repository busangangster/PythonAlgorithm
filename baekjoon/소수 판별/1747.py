# 소수보다 펠린드롬의 갯수가 더 많기 때문에 판별해줄 때 펠린드롬부터 하는게 
# 시간 복잡도 측면에서 효율적

n = int(input())

def isPrime(n):
  if n == 1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  else:
    return True

def isPal(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False

for i in range(n,1000001):
  if i == 1000000:
    print(1003001)
  if isPal(i):
    if isPrime(i):
      print(i)
      break