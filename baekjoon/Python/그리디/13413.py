import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  a = list(input().strip())
  b = list(input().strip())
  cnt = []
  
  for i in range(n):
    if a[i] != b[i]:
      cnt.append(a[i])

  if not cnt:
    print(0)
  
  elif cnt.count('B') > cnt.count('W'):
    print(cnt.count('B'))
  
  else:
    print(cnt.count('W'))