import sys
input = sys.stdin.readline

k = int(input())

a = 0
b = 1
for i in range(k-1):
  a,b = b,a+b

print(b)

#재귀 -> 시간초과
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

print(fibo(k))


