import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

for i in range(1,n):
  # 해당 인덱스의 값과 이전의 값들의 합을 비교하여
  # 최댓값을 기록
  a[i] = max(a[i], a[i] + a[i-1])

print(max(a))


