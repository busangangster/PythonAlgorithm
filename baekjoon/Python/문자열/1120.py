import sys
input = sys.stdin.readline

a,b = map(str,input().split())
a = list(a)
b = list(b)
cnt = 0

if len(a) != len(b):
  while len(a) != len(b):
    if a[0] == b[0]:
      a.append()
    elif a[-1] == b[-1]:
      a.insert(0,b[len(b)-len(a)-1])

      
      



else:
  for i in range(len(a)):
    if a[i] != b[i]:
      cnt += 1

  print(cnt)
