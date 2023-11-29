import sys
input = sys.stdin.readline

n = int(input())
t = ['4','7']
for i in range(n,0,-1):
  for x in str(i):
    if x not in t:
      break
  else:
    print(i)
    break