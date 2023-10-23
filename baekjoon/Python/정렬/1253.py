import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort() # 투 포인터를 사용하기 위해 정렬 
cnt = 0

for i in range(n): # 입력 받은 배열의 모든 수를 확인해줘야 함 
  tmp = a[:i] + a[i+1:] # 해당 수를 제외한 다른 수들로 리스트를 생성 
  left = 0
  right = len(tmp)-1 
  while left < right: # 투 포인터 실행 
    mid = tmp[left] + tmp[right]

    if mid == a[i]: # 같은 값 찾으면 cnt 1 올리고 반복문 바로 빠져나옴
      cnt += 1
      break
    elif mid > a[i]:
      right -= 1
    else:
      left += 1

print(cnt)