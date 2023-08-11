import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
arr = []
ans = ''

for i in a: # 리스트의 원소들을 문자열 형태로 만들어 배열에 추가
  arr.append(str(i))
  
# 배열을 내림차순 정렬하는데, 문자열에 10을 곱한 값을 기준으로 정렬.
arr.sort(key = lambda x:x*10, reverse = True)

# 정렬한 순서대로 ans에 더해줌 
for i in arr:
  ans += i

# ans가 문자열인데, 이를 정수형으로 출력해야 조건에 맞출 수 있음
print(int(ans))




