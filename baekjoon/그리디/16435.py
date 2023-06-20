import sys
input = sys.stdin.readline

n, l = map(int,input().split())
a = sorted(list(map(int,input().split())))


for x in a:
  if l >= x:
    l += 1

print(l)