import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
  a,b,c,d = map(int,input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

ab_dic = {}
ans = 0

for i in A: # a와 b로 만들 수 있는 모든 경우의 수 
  for j in B:
    if (i+j) in ab_dic:
      ab_dic[i+j] += 1
    else:
      ab_dic[i+j] = 1

for i in C: # c와 d로 만들 수 있는 모든 경우
  for j in D:
    ans += ab_dic.get(-(i+j),0)

print(ans)
