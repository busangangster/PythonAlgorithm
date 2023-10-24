import sys
input = sys.stdin.readline

n,l = map(int,input().split())
a = sorted(list(map(int,input().split())))
cnt = 1
start = a[0]

for x in a[1:]:
  if x not in range(start,start+l):
    start = x
    cnt += 1

print(cnt)