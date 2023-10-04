import sys
input = sys.stdin.readline

n,c = map(int,input().split())
dict = {}
a = list(map(int,input().split()))

for i in a:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1

# 딕셔너리의 value 값을 기준으로 내림차순 정렬 
dd = sorted(dict.items(), key = lambda x:x[1],reverse=True)

for i in dd:
  for j in range(i[1]):
    print(i[0],end=' ')
