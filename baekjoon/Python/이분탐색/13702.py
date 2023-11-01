import sys
input = sys.stdin.readline

def binary(a,k):
  lt = 1
  rt = max(a)
  ans = 0
  while lt <= rt:
    cnt = 0
    mid = (lt+rt) // 2

    for x in a:
      cnt += (x // mid)
    
    if cnt >= k:
      ans = mid
      lt = mid + 1
    else:
      rt = mid - 1

  return ans
  
n,k = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

print(binary(arr,k))