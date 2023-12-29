import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

if a == 2 and b == 18:
  print('Special')
elif a <= 2:
  print('Before')
elif a <= 2 and b <= 18:
  print('Before')
else:
  print('After')