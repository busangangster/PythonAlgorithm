import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  a,b = map(int,input().split())
  sum = 0
  if a == 1:
    sum += 5000000
  if 1 < a <= 3:
    sum += 3000000
  if 3 < a <= 6:
    sum += 2000000
  if 6 < a <= 10:
    sum += 500000
  if 10 < a <= 15:
    sum += 300000
  if 15 < a <= 21:
    sum += 100000
  if b == 1:
    sum += 5120000
  if 1 < b <= 3:
    sum += 2560000
  if 3< b <= 7:
    sum += 1280000
  if 7 < b <= 15:
    sum += 640000
  if 15 < b <= 31:
    sum += 320000
  print(sum)
  