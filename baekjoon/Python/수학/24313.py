import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c = int(input())
n = int(input())

for i in range(n,100):
  if a*i + b > c*i:
    print(0)
    break
else:
  print(1)