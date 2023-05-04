import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())))
  
k = int(input())

for _ in range(k):
  ans = 0
  i,j,x,y = map(int,input().split())
  for k in range(i-1,x):
    for t in range(j-1,y):
      ans += arr[k][t]
  
  print(ans)




