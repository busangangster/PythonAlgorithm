import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
dic = {}
max_v = 0
min_v = 0

for _ in range(n):
  a,b = map(str,input().split())
  b = int(b)
  dic[a] = b

for _ in range(k):
  t = input().strip()
  max_v += dic[t] # 공개된 과목의 점수를 최대,최소에 각각 저장
  min_v += dic[t]
  del dic[t] # 공개된 과목은 더이상 필요없음 

# 브실이가 수강한 과목을 점수 순대로 오름차순, 내림차순 정렬 
arr1 = sorted(dic.items(),key = lambda x: x[1])
arr2 = sorted(dic.items(),key = lambda x: -x[1])

for i in range(m-k): # 최솟값 구하기
  min_v += arr1[i][1]

for i in range(m-k): # 최댓값 구하기 
  max_v += arr2[i][1]

print(min_v,max_v)