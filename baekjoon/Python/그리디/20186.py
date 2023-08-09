import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
res = []

# 가장 큰 수부터 뽑는 경우 전체점수를 최대로 만들 수 있음
a.sort(reverse = True) 

for i in range(k): # 정렬 된 리스트에서 k만큼 뽑기
  res.append(a[i])

cnt = 0
sum = 0

for i in res:
  # 고른 수 중 자신의 왼쪽에 있는 수의 개수만큼 뺴줘야함 
  sum += i - (len(res) - (len(res)-cnt))
  cnt += 1

print(sum)

