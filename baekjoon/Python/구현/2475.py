import sys
input = sys.stdin.readline

a = list(map(int,input().split()))
sum = 0
for x in a:
  sum += x**2

print(sum % 10 )
