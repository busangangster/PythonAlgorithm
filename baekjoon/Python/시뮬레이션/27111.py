import sys
input = sys.stdin.readline

n = int(input())
ans = [10] * 200001
cnt = 0
for i in range(n):
  a,b = map(int,input().split())
  if b == 1:
    if ans[a] == 1:
      cnt += 1
    else:
      ans[a] = 1
  else:
    if ans[a] == 10:
      cnt += 1
    elif ans[a] == 1:
      ans[a] = 0
    elif ans[a] == 0:
      cnt += 1
             
cnt += ans.count(1)

print(cnt)