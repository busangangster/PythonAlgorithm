

import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  a,b = map(int,input().split())
  ans = a*b
  while b != 0: # 주어진 두 수의 최대공약수 찾기
    r = a % b
    a = b
    b = r
  # 최소공배수 = 두 자연수의 곱 // 최대공약수
  print(ans//a) # 최소공배수 구하기
  

  