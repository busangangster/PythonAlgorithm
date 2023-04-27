import sys
input = sys.stdin.readline

n = int(input())

def fibo(k):
  a = 0
  b = 1
  if k == 0:
    return 0
  elif k == 1 or k ==2:
    return 1
  else:
    for _ in range(k):
      a,b = b, a+b
    return a

print(fibo(n))