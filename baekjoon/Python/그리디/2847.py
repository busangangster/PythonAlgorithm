import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n): # 입력받은 레벨 리스트에 append
  arr.append(int(input()))

cnt = 0 # 횟수 세는 변수 

for i in range(n-1,0,-1): # 뒤에서부터 접근 
  # 현재 레벨의 점수가 그 전 레벨의 점수보다 작거나 같다면
  if arr[i] <= arr[i-1]:
    # 그전 레벨의 점수를 낮춰줘야 하기 때문에
    # cnt에 현재 바로 앞 점수 - 현재 점수 + 1을 해줌
    cnt += arr[i-1] - arr[i] + 1
    # 앞 점수는 현재점수보다 낮아야 하기에 -1 
    arr[i-1] = arr[i] - 1

print(cnt)


  