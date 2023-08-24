# 삼각형 만들 수 있는 조건: 세 변이 주어졌을 때 가장 긴 변이 다른 두변의 합보다 작아야함
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse= True)

while arr:
  if len(arr) >= 3 and arr[0] < arr[1] + arr[2]:
    print(arr[0]+arr[1]+arr[2])
    break
  else:
    arr.pop(0)
else:
  print(-1)