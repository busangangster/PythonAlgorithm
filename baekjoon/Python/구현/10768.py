import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

if a == 2 and b == 18:
  print('Special')
elif a ==1:
  print('Before')
elif a in [1,2] and b <= 18:
  print('Before')
else:
  print('After')