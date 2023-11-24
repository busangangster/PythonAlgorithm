import sys
input = sys.stdin.readline

while True:
  s = input().rstrip('\n')
  if not s:
    break
  a,b,c,d=0,0,0,0
  for x in s:
    if x.isdigit():
      c +=1
    elif x.isupper():
      b += 1
    elif x.islower():
      a += 1
    elif x == ' ':
      d += 1

  print(a,b,c,d)
  
  