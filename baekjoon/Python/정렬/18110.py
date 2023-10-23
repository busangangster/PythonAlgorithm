import sys
input = sys.stdin.readline

n = int(input())
num = []

def a(x):
  if (x - int(x)) >= 0.5:
    return int(x) + 1
  else:
    return int(x)

if n != 0:
  for _ in range(n):
    num.append(int(input()))

  num.sort()
  k = a(n*0.15)

  if k != 0:
    num = num[k:-k]

  print(a(sum(num) / len(num)))

else:
  print(0)