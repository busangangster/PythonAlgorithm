# import sys
# input = sys.stdin.readline

t = int(input())
for t_case in range(1,t+1):
  n,s,e,k = map(int,input().split())
  a = list(map(int,input().split()))
  aa = a[s-1:e]
  aa.sort()
  for i,j in enumerate(aa):
    if i == k-1:
      print('#{} {}'.format(t_case,j))
