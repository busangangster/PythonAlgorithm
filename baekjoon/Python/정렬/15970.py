import sys
input = sys.stdin.readline

n  =  int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  ans += min([abs(arr[x][0] - arr[i][0]) for x in range(n) 
              if arr[x][1] == arr[i][1] and x != i])

print(ans)