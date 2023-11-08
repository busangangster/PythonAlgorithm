import sys
n = int(input())
box = 0
cnt = 0

for _ in range(n):
  t,w,h,l = map(str,input().split())
  w,h,l = int(w),int(h),int(l)
  if t == 'A':
    cnt += (w //12) * (h // 12) * (l // 12) # 상자 안에 채울 수 있는 사과 양
    box += 1000
  else:
    box += 120 * 50 # 배인 경우 상자 질량만 계산

box += cnt * 500  # 상자 질량
price = cnt * 4000 # 사과 가격
print(box)
print(price)
