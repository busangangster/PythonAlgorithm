import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

ans = []

for i in range(n):
  cnt = 0
  for j in range(i+1,n):
    if a[i] > a[j]:
      cnt += 1
    else:
      break
  ans.append(cnt)

print(max(ans))



      
