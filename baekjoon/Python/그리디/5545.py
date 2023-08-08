import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
c = int(input())
topping = []

for _ in range(n):
  topping.append(int(input()))

topping.sort(reverse = True)
ans = c / a # 초기값을 아무 토핑도 추가하지 않았을 때로 설정 

for i in range(1,len(topping)+1):
  # 토핑을 추가할 때마다 칼로리가 올라가는데, 감소하는 시점이 존재함 ! 
  # 감소하기 바로 전까지만 토핑을 추가한 칼로리가 답이 됨. 
  cal = c + sum(topping[0:i])
  p = a + b * i

  if cal / p > ans:
    ans = cal / p
  else:
    break

print(int(ans))

   