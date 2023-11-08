import sys
input = sys.stdin.readline

while True:
  n = int(input())
  if n == -1:
    break
  else:
    s = []
    for i in range(1,n):
      if n % i == 0:
        s.append(i)
    
    if sum(s) == n:
      print('{} ='.format(n),end=' ')
      for x in s:
        if x == s[-1]:
          print(x)  
        else:
          print('{} +'.format(x),end=' ')
    else:
      print('{} is NOT perfect.'.format(n))