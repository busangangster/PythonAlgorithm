

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for x in b:
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt+rt) // 2
        if x == a[mid]:
            print(1)
            break
        elif a[mid] > x:
            rt = mid - 1
        else: 
            lt = mid + 1
    else:
      print(0)










for x in b:
  if x in a:
    print(1)
  else:
    print(0)