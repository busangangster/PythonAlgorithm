import sys
n = int(sys.stdin.readline())
a = []
et = 0
cnt = 0

for _ in range(n):
  tmp = list(map(int,sys.stdin.readline().split()))
  a.append(tmp)

# 리스트를 끝나는 시간 기준으로 오름차순 정렬
a.sort(key = lambda x: (x[1],x[0]))

# 회의의 시작시간이 그 전 회의의 끝나는 시간보다 크거나 같아야 함 
for i in a:
  if i[0] >= et:
    et = i[1]
    cnt += 1

print(cnt)