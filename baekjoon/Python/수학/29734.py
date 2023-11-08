import sys
input = sys.stdin.readline

n,m = map(int,input().split())
x,s = map(int,input().split())

if n % 8 == 0: # 과제하는 시간을 일할 수 있는 시간으로 나눈 나머지가 0이면
  z = n // 8 - 1 # 잠을 한번 더 안자고 과제 제출 가능
else: # 그게 아니면 잠 함 더 자고 과제 마무리 및 제출해야 함 
  z = n // 8

if m % 8 == 0:
  k = m // 8 - 1
else:
  k = m // 8

zip = n + (s*z)
dok = x + m + (k*s) + (k*2*x) # 독서실은 집이랑 왔다갔다 하면서 과제해야 함

if zip < dok:
  print('Zip')
  print(zip)
else:
  print('Dok')
  print(dok)