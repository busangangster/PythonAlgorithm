import sys
n = int(sys.stdin.readline())

plus = [] # 양수 배열
minus = [] # 음수 배열
ans = 0 # 결과값 변수

# 입력 받는 수를 양수, 음수 또는 0, 1로 나누는 반복문
for i in range(n):
  a = int(sys.stdin.readline())
  if a > 1:
    plus.append(a)
  elif a <= 0:
    minus.append(a)
  else:
    ans += a
  
plus.sort(reverse = True) # 큰 수부터 곱하기
minus.sort() # 작은 수부터 곱하기

# 양수 배열과 음수 배열에 있는 수들을 2개씩 곱해서 결과값에 더해줌
# 하나가 남았을 경우에는 결과값이 '플러스' 해줌 
for i in range(0,len(plus),2):
  if i+1 >= len(plus):
    ans += plus[i]
  else:
    ans += (plus[i] * plus[i+1])

for i in range(0,len(minus),2):
  if i+1 >= len(minus):
    ans += minus[i]
  else:
    ans += (minus[i] * minus[i+1])

print(ans)




