import sys
input = sys.stdin.readline

money = int(input())
a = list(map(int,input().split()))

def jun():
  left_money = money
  stock = 0
  for x in a:
    stock += left_money // x
    left_money = left_money % x
    if left_money == 0:
      break
  return left_money,stock

def sung():
  left_money = money
  stock = 0
  for i in range(len(a)-4):
    if a[i] < a[i+1] < a[i+2] < a[i+3]: # 계속 상승 
      left_money += stock * a[i+3]
      stock = 0

    if a[i] > a[i+1] > a[i+2] > a[i+3]: # 계속 하락
      stock += left_money // a[i+3]
      left_money = left_money % a[i+3]
      
  return left_money,stock

j_money,j_stock = jun()
t = j_money + j_stock * a[-1]
s_money,s_stock = sung()
k = s_money + s_stock * a[-1]

if t > k:
  print('BNP')
elif t < k:
  print('TIMING')
else:
  print('SAMESAME')
