import sys
n = int(input())
box = 0
cnt = 0
count =0
for _ in range(n):
  t,w,h,l = map(str,input().split())
  w,h,l = int(w),int(h),int(l)
  if t == 'A':
    cnt += (w //12) * (h // 12) * (l // 12)
    count += 1
  else:
    box += 120 * 50

box += (1000 * count) + (cnt*500) 
price = cnt * 4000
print(box)
print(price)