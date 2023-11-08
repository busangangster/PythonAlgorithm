import sys
input = sys.stdin.readline

s,n,m = map(int,input().split())
arr = []
for _ in range(n+m):
  k = int(input())
  if k == 1: # 1인 경우에 배열에 추가하는데
    if len(arr) == s: # 배열의 크기가 배열의 최대 크기와 같으면
      s *= 2 # 크기 2배 증가시킨 뒤, 배열에 추가 
    arr.append(k) 
  else: # 0일 경우 배열에서 제거
    arr.pop()

print(s)