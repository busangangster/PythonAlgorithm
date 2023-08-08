import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
dict = {'R':0, 'B':0} # Blue or Red로 색칠하는 횟수를 세는 딕셔너리
dict[a[0]] += 1 # 처음 나오는 색을 칠해줘야 그 다음 색과 비교할 수 있음 

for i in range(1,n):
  if a[i] != a[i-1]: # 현재 색이 이전 색과 다르다면, 그 색을 칠해줘야 함 
    dict[a[i]] += 1 # 딕셔너리에서 해당 색을 1 증가 

# 1을 더하는 이뉴는 전체를 색칠해준 뒤, 색을 나눠 칠해야하기 때문에 ! 
ans = min(dict['B'], dict['R']) + 1 
print(ans)
    



