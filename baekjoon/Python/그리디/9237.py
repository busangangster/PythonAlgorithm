import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
tree = [] # 나무가 다 자라기까지 며칠이 걸리는지
day = 1 # 첫 묘목을 심는 날은 1일 

# 다 자라기까지 가장 오래 걸리는 묘목을 먼저 심어야 함 
a.sort(reverse = True) 

for i in range(n):
  tree.append(a[i]+day)
  day += 1 # 하루에 묘목 하나씩 심기 때문에 day가 1씩 증가

print(max(tree) +1) # 나무가 다 자란 뒤 이장님을 초대해야 하기 때문에 + 1
  


