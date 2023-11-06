import sys
input = sys.stdin.readline
a = list(input().strip())
t = a.count('0') // 2
k = a.count('1') // 2

a = a[::-1] # 0은 뒤에서부터 제거
for _ in range(t):
  a.pop(a.index('0'))

a = a[::-1] # 1은 앞에서부터 제거
for _ in range(k):
  a.pop(a.index('1'))

print(''.join(map(str,a)))