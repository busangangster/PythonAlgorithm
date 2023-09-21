import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = 0

if a < 0:
  ans += abs(a) * c
  ans += d
  ans += b * e

else:
  ans += (b-a) * e
  
print(ans)