import sys
input = sys.stdin.readline

m = []
for _ in range(5):
  m.append(int(input()))

price = []
for i in range(3):
  price.append(m[i]+m[-1]-50)
  price.append(m[i]+m[-2]-50)

print(min(price))