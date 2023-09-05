import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = a[:]
t = b[:]
lar = 0
sm = 0
# 가장 큰 수 
while b[1] != 0:
  lar = a[0] - a[1]
  a.pop(0)
  a.pop(0)
  a.insert(0,lar)
  b[1] -= 1

while b[3] != 0:
  if a[0] < 0:
    a[0] = -a[0]
    lar = -(a[0] // a[1])
    a.pop(0)
    a.pop(0)
    a.insert(0,lar)
  else:
    lar = (a[0] // a[1])
    a.pop(0)
    a.pop(0)
    a.insert(0,lar)
  b[3] -= 1 

while b[0] != 0:
  lar = a[0] + a[1]
  a.pop(0)
  a.pop(0)
  a.insert(0,lar)
  b[0] -= 1

while b[2] != 0:
  lar = a[0] * a[1]
  a.pop(0)
  a.pop(0)
  a.insert(0,lar)
  b[2] -= 1

print(lar)

while t[0] != 0:
  sm = k[0] + k[1]
  k.pop(0)
  k.pop(0)
  k.insert(0,sm)
  t[0] -= 1

while t[3] != 0:
  if k[0] < 0:
    k[0] = -k[0]
    sm = -(k[0] // k[1])
    k.pop(0)
    k.pop(0)
    k.insert(0,sm)
  else:
    sm = (k[0] // k[1])
    k.pop(0)
    k.pop(0)
    k.insert(0,sm)
  t[3] -= 1 

while t[1] != 0:
  sm = k[0] - k[1]
  k.pop(0)
  k.pop(0)
  k.insert(0,sm)
  t[1] -= 1

while t[2] != 0:
  sm = k[0] * k[1]
  k.pop(0)
  k.pop(0)
  k.insert(0,sm)
  t[2] -= 1

print(sm)