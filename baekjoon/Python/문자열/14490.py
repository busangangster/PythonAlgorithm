import sys
input = sys.stdin.readline
s = input().strip().split(':')

def gcd(a,b):
  while b > 0:
    a,b = b,a%b
  return a

first = int(s[0])
second = int(s[1])
k = gcd(first,second)

print("{}:{}".format(first//k,second//k))