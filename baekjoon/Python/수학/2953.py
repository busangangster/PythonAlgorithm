import sys
input = sys.stdin.readline

ans = []
for i in range(1,6):
  a = list(map(int,input().split()))
  ans.append([i,sum(a)])

ans.sort(key = lambda x:-x[1])
print(*ans[0])