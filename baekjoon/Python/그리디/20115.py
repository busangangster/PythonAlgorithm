import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = 0
a.sort() # 양이 가장 작은 것과 큰 것을 합치기 위한 정렬

while len(a) != 1:
  # 두개를 합칠 때 작은 양은 반을 더하고, 큰 양은 그대로 더해줌 
  ans = a.pop()  + (a.pop(0) / 2 ) 
  a.append(ans)

print(ans)

