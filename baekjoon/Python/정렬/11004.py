import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
h = n // 2

if k > h:
  a.sort(reverse=True)
  print(a[-k])

else:
  a.sort()
  print(a[k-1])
