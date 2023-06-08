import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
cnt = 0

for i in range(len(a)):
  if a[i] == cnt%3:
    cnt += 1

print(cnt)
