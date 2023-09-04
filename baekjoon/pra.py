import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def GCD(n,m):
  while m != 0:
    r = n%m
    n = m
    m = r
  return n

print(GCD(b,a))
print(a*b//GCD(b,a))

