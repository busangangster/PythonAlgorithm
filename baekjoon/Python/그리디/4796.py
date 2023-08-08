import sys
input = sys.stdin.readline

i = 1
while True:
  l,p,v = map(int,input().split())
  cnt = 0
  if l == 0  and p == 0 and v == 0:
    break
  a = v//p
  b = v%p
  if b > l:
    b = l
  res = a*l + b
  print('Case %s: %d' %(i,res))
  i += 1
  
  


  
  