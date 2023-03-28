
import sys

n,m = map(int,sys.stdin.readline().split())
a = [i for i in range(1,n+1)]

for _ in range(m):
  i,j,k = map(int,sys.stdin.readline().split())
  a[i-1:j] = a[k-1:j] + a[i-1:k-1]

for x in a:
  print(x,end=' ')


