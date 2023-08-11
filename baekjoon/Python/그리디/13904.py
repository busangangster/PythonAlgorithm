import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
check = [False] * 1001

for _ in range(n):
  d,w = map(int,input().split())
  arr.append([d,w])

arr.sort(key = lambda x: x[1], reverse = True)


for i,k in arr:
  day = i 
  while day > 0 and check[day]:
    day -= 1

  if day == 0: # 과제를 넣을 자리 없음
    pass
  else:
    check[day] = True
    ans += k

print(ans)




    