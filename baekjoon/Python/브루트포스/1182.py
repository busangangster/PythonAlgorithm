import sys
import itertools 
input = sys.stdin.readline
n,s = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0

for i in range(1,n+1):
  ans = itertools.combinations(a,i)
  for x in ans:
    if sum(x) == s:
      cnt += 1
print(cnt)