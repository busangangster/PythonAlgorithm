import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
ans = 0

for i in a:
  k = i - b 
  ans += 1 # 시험장에 총감독은 무조건 한명씩 있어야함
  if k <= 0: # 시험장 응시생 수가 총감독이 감독할 수 있는 수보다 작으면
    continue
    
  else: # 부감독이 필요할 때 
    if k%c == 0: 
      ans += k //c 
    else:
      ans += (k//c + 1)

print(ans)


