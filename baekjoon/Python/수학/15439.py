import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(n):
  for j in range(i+1,n):
    cnt += 1

print(cnt*2)