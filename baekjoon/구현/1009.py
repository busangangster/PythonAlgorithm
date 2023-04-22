import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  a,b = map(int,input().split())
  a = a % 10
  
  if a == 0:
    print(10)
  elif a in [1,5,6]:
    print(a)
  elif a in [4,9]:
    if b % 2 == 0: # b가 짝수일 때
      print(a*a%10)
    else:
      print(a)
  elif a in [2,3,7,8]:
    if b%4 == 0:
      print(a**4%10)
    else:
      print(a**b%10)



