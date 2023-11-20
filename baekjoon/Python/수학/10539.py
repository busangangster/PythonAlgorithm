import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = [a[0]]
k = 2

for i in range(1,n):
  cnt = sum(ans)
  ans.append(a[i]*k - cnt)
  k += 1
print(*ans)