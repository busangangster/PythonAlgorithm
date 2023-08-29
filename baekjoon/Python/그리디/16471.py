import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split())) # 주언
b = list(map(int,input().split())) # 사장
cnt = 0

a.sort()
b.sort()
k = (n+1) // 2

for i in range((n+1)//2):
  if a[i] < b[-k]:
    cnt += 1
    k -= 1

if cnt >= (n+1) // 2:
  print('YES')
else:
  print('NO')
  
  

