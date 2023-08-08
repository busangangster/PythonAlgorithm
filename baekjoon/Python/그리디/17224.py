

import sys
input = sys.stdin.readline

n,l,k = map(int,input().split())
p = []
score = 0
cnt = 0
for _ in range(n):
  p.append(list(map(int,input().split())))

p.sort(key = lambda x:x[1]) # 어려운 문제 순으로 오름차순 정렬 

for x in p:
  if cnt == k:
    break
  if x[1] <= l: # 어려운 문제를 풀 수 있다면 쉬운 문제도 풀 수 있음
    score += 140 # 따라서 140점 플러스
    cnt += 1
  elif x[0] <= l: # 쉬운문제만 풀 수 있는 경우
    score += 100 # 100점 플러스 
    cnt += 1

print(score)
      


  