import sys

n = int(sys.stdin.readline())

distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))
money = 0
least = 2147000000

for i in range(n-1):
  if price[i] <= least:
    least = price[i]
  money += least * distance[i]

print(money)
