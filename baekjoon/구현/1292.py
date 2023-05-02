import sys
input = sys.stdin.readline

ans = 0
arr = []
a,b = map(int,input().split())

for i in range(1,100):
  for j in range(i):
    arr.append(i)

for k in range(a-1,b):
  ans += arr[k]

print(ans)

  
  

