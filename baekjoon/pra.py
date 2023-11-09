import sys
import copy
input = sys.stdin.readline

n,m,k = map(int,input().split())
a = [0] + list(input().strip())
aa = copy.deepcopy(a)

for i in range(1,n+1):
  if a[i] == 'R':
    t,g = max(1,i-k),min(n,i+k)
    for j in range(t,g+1):
      aa[j] = 'R'

if aa.count('R') <= m:
  print('Yes')
else:
  print('No')   
