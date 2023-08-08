

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for x in b:
  lt = 0
  rt = n -1
  while lt <= rt:
    mid = (lt+rt) // 2
    if x == a[mid]:
      print(1,end=' ')
      break
    elif x > a[mid]:
      lt = mid +1
    else:
      rt = mid - 1
  else:
    print(0,end=' ')


