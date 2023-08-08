import sys
from collections import Counter 
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
  a.append(int(input()))

a.sort()

print(round(sum(a)/n)) # 산술평균 출력
print(a[len(a)//2]) # 중앙값 출력

cnt = Counter(a).most_common(2)


if len(cnt) > 1: # 최빈값 출력
  if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(cnt[0][0])

print(abs(a[0] - a[-1])) # 범위 출력
