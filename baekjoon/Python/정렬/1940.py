import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int,input().split()))
left = 0
right = n-1
cnt = 0
a.sort()

while True:
  if left >= right:
    break
  
  cur = a[left] + a[right]

  if cur == m:
    cnt += 1
    right -= 1

  elif cur < m:
    left += 1
  
  else:
    right -= 1

print(cnt)