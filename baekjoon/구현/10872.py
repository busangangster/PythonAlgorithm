import sys
input = sys.stdin.readline

# 재귀 
n = int(input())

def fac(k):
  if k == 0:
    return 1
  else:
    return k * fac(k-1)
  
print(fac(n))

# 반복문
ans = 1

if n == 0:
  print(1)
else:
  for i in range(1,n+1):
    ans = ans* i
  print(ans)


