# ord()함수: 문자를 인자로 받고, 해당 문자에 해당하는 유니코드 정수 반환
def isPrime(n):
  if n == 1:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  else:
    return True

n = input()
k = 0

for x in n:
  if x.isupper():
    k += (ord(x)-38) #ord('A')는 65임 
  else:
    k += (ord(x)-96)

if isPrime(k):
  print('It is a prime word.')
else:
  print("It is not a prime word.")

    