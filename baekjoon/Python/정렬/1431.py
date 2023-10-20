

import sys
input = sys.stdin.readline

n = int(input())
a = [list(input().strip()) for _ in range(n)]

for i in a: 
  ans = 0
  for j in i: # 자릿수의 합을 구해서 시리얼 번호 마지막에 저장 
    if j.isdigit():
      ans += int(j)
  i.append(ans)

# 문제에서 주어진 조건대로 정렬 
a.sort(key = lambda x:(len(x),x[-1],x))

for x in a:
  x.pop() # 자리수의 합은 제거하고 
  print(''.join(map(str,x))) # 시리얼 번호는 출력 


