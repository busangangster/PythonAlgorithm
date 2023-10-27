import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
ans = [0]

def binary(k):
  lt = 0
  rt = len(ans)-1

  while lt <= rt:
    mid = (lt+rt) // 2

    if ans[mid] >= k:
      rt = mid -1
    else:
      lt = mid + 1
      
  return rt + 1

for x in a:
  if ans[-1] < x:
    ans.append(x)
  else:
    ans[binary(x)] = x
  
print(len(ans)-1)