import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
arr = []
check = []

for _ in range(n):
  arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[1])

for i in arr:
  hq.heappush(check,i[0])
  if len(check) > i[1]: # 날짜를 최소힙의 길이로 설정 
    hq.heappop(check)

print(sum(check))

