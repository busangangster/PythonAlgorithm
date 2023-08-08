import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dict = {}

for i in arr: # 딕셔너리 안에 key가 있으면 +1씩 증가
  dict[i] = dict.get(i,0) + 1

# 가장 높은 value값을 출력
print(max(dict.values()))



