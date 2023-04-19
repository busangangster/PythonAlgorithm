import sys
t = int(sys.stdin.readline())
a = [300,60,10]

# 300,60,10의 최대공약수는 10 
if t%10 != 0:
  print(-1)
else:
  for i in a:
    print(t//i,end=' ')
    t = t%i