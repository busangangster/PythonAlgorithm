import sys
input = sys.stdin.readline

t = int(input())

def fac(n):
  if n == 1:
    return 1
  else:
    return n * fac(n-1)

factorial = str(fac(t))
cnt = 0
for i in range(len(factorial)-1,-1,-1):
  if factorial[i] != '0':
    print(cnt)
    break
  else:
    cnt += 1