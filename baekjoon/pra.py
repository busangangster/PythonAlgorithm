import sys
input = sys.stdin.readline

n,x,k = map(int,input().split())
b = [0] * (n+1)
b[x] = 1

print(b)

for _ in range(k):
  x,y = map(int,input().split())
  b[x],b[y] = b[y],b[x]


for x in range(len(b)):
  if b[x] == 1:
    print(x)
