import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
x = int(input())
cnt = 0
a.sort()
first = 0
last = n-1

while True:
  if first >= last:
    break
  
  cur = a[first] + a[last]
  if cur == x:
    cnt += 1
    first += 1
  elif cur < x:
    first += 1
  else:
    last -= 1

print(cnt)