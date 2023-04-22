import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n):
  val = input().strip().split()
  
  if len(val) == 1:
    if val[0] == 'all':
      s = set(range(1,21))
    else:
      s = set()
      
  else:
    a,b = val[0],int(val[1])
    if a == 'add':
      s.add(b)
    elif a == 'remove':
      s.discard(b)
    elif a == 'check':
      if b in s:
        print(1)
      else:
        print(0)
    elif a == 'toggle':
      if b in s:
        s.discard(b)
      else:
        s.add(b)

    
    


      

