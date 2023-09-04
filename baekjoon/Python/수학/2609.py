# GCD: 유클리드 호제법. 최대공약수 구하는 공식 

import sys
input = sys.stdin.readline
a,b = map(int,input().split())

def GCD(t,k): # 최대공약수 구하는 함수
  while k != 0: # 유클리드 호제법
    r = t % k
    t = k
    k = r 
  return t

print(GCD(b,a)) # 최대공약수 출력
print(a*b//GCD(b,a)) # 최소공배수 출력

  

