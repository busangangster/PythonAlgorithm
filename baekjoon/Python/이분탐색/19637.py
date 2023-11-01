import sys
input = sys.stdin.readline

n,m = map(int,input().split())
rank = [list(input().split()) for _ in range(n)]

def binary(rank,a):
  lt = 0
  rt = n - 1
  ans = 0
  while lt <= rt:
    mid = (lt+rt) // 2

    if int(rank[mid][1]) >= a:
      rt = mid - 1
      ans = mid

    else:
      lt = mid + 1
  return rank[ans][0]


for _ in range(m):
  a = int(input())
  print(binary(rank,a))