import sys
input = sys.stdin.readline

n,k = map(int,input().split())

a = []

for i in range(1,n+1):
  if n % i == 0:
    a.append(i)

for idx,val in enumerate(a):
  if idx == k-1:
    print(val)
    break
else:
  print(0)
