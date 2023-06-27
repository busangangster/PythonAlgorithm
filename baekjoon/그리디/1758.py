

import sys
input = sys.stdin.readline

n = int(input())
arr = [] # 원래 주고자 하는 팁 리스트 
tips = 0

for _ in range(n):
  arr.append(int(input()))

# 주려고 하는 돈이 큰 순서대로 내림차순 정렬 
arr.sort(reverse = True)

for i in range(1,n+1): # 입구에 들어가는 순서 i 
  if arr[0] - (i-1) > 0: # 만약 팁이 양수일 경우 
    tips += arr[0] - (i-1) # 팁을 추가해줌. 
    arr.pop(0) 
  else: # 음수일 경우 
    arr.pop(0)

print(tips)




