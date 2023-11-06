import sys
input = sys.stdin.readline
m = []
n = int(input())
for _ in range(n):
  a,b,c = map(int,input().split())
  money = 0
  if a == b == c:
    money += 10000 + a * 1000
  elif a == b and b != c:
    money += 1000 + a*100
  elif a != b and b == c:
    money += 1000 + b*100
  elif a == c and b != c:
    money += 1000 + a*100
  elif a != b and b != c:
    money += max(a,b,c)*100
  
  m.append(money)
print(max(m))
    