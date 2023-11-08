import sys
input = sys.stdin.readline

n,m = map(int,input().split())
x,y = map(int,input().split())
password = [0 for _ in range(n+1)]
number = []
# if m == 0:

# else:
for _ in range(m):
  a,b = map(int,input().split())
  if a == 0:
    number.append(b)
  else:
    password[a] = b
password.pop(0)
t = password.count(0)
k = 1
if t == len(number):
  for i in range(t,0,-1):
    k *= i
else:
  