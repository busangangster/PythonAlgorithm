

import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n): 
  a = list(input().strip()) 
  s1 = []
  s2 = []
  for x in a:
    if x == '<':
      if s1:
        s2.append(s1.pop())

    elif x == '>':
      if s2:
        s1.append(s2.pop())

    elif x == '-':
      if s1:
        s1.pop()

    else:
      s1.append(x)
    
  s1.extend(reversed(s2))
  print(''.join(s1))


  

