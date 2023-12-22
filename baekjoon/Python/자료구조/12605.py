import sys
input = sys.stdin.readline

n = int(input())
for tc in range(1,n+1):
  s = list(map(str,input().strip().split(" ")))
  print('Case #{}:'.format(tc),end=' ')
  print(*s[::-1])