import sys
input = sys.stdin.readline

def lower_bound(a,target): # 이분탐색 lower_bound 구현 
  lt,rt = 0, len(a)-1

  while lt <= rt:
    mid = (lt+rt) // 2
    if a[mid] < target:
      lt = mid + 1
    elif a[mid] > target:
      rt = mid -1
    elif a[mid] == target:
      if rt == mid:
        break
      rt = mid 

  if a[mid] == target:
    return mid
  else:
    return -1
  
n,m = map(int,input().split())
a = []
for _ in range(n):
  a.append(int(input()))

a.sort()
for _ in range(m):
  k = int(input())
  print(lower_bound(a,k))



