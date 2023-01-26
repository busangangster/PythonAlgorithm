import sys

n,c = map(int,sys.stdin.readline().split())
a = []
res = 0
for i in range(n):
  tmp = int(sys.stdin.readline())
  a.append(tmp)

a.sort()

lt = 1
rt = max(a)

def Count(x):
  cnt = 1 # 제일 처음 집에 공유기 하나 설치하고 시작 
  k = a[0] # 집 사이의 거리 비교를 위한 변수 k 선언 
  for i in a:
    if i-k >= mid: # 집과 집 사이의 거리가 중간값보다 크거나 같으면 공유기 설치 가능
      cnt += 1
      k = i # 공유기가 설치된 위치 저장 
  return cnt

while lt <= rt:
  mid = (lt+rt) // 2
  if Count(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid -1

print(res)

