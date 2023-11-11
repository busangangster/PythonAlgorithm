import sys
input = sys.stdin.readline

n = int(input())
cnt= 0 
a = list(map(str,input().split()))
for x in a:
  if x[0] == str(n):
    cnt += 1

print(cnt)