# 10진수를 2진수로 바꾸는 함수: bin
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  k = list(bin(n)[2:][::-1]) # 2진수는 문자열 형태로 나옴
    
  for idx, val in enumerate(k):
    if val == '1':
      print(idx,end=' ')
  