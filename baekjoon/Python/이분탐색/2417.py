import sys
input = sys.stdin.readline

n = int(input())
lt = 0
rt = n
ans = 0
while lt <= rt:
  mid = (lt+rt) // 2
  
  if mid**2 >= n:
    ans = mid
    rt = mid-1 
  else:
    lt = mid + 1

print(ans)
