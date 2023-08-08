import sys
input = sys.stdin.readline

n = int(input())

arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
  a,b = map(int,input().split())
  for i in range(a,a+10):
    for j in range(b,b+10):
      arr[i][j] = 1

ans = 0

for rows in arr:
  ans += sum(rows)

print(arr)
print(ans)