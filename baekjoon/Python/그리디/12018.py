import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []

for _ in range(n):
  p,l = map(int,input().split())
  a = list(map(int,input().split()))
  a.sort(reverse = True)
  if len(a) >= l-1: # 과목에 신청한 사람이 수강인원보다 클 때
    ans.append(a[l-1]) # 과목에 마일리지를 l-1번째로 투자한 사람과 똑같이 사용해야 함
  else: # 과목에 신청한 사람이 수강인원보다 작을 때
    ans.append(1) # 최소 마일리지로 과목을 수강함 

ans.sort() # 성준이가 과목별로 사용해야 할 마일리지들 오름차순 정렬
cnt = 0

# 가지고 있는 마일리지를 사용하면서 들을 수 있는 과목을 체크 
for x in ans: 
  if x <= m:
    m -= x
    cnt +=1

print(cnt)






