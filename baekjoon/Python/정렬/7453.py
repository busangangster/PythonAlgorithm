import sys
input = sys.stdin.readline

n = int(input())
A,B,C,D = [],[],[],[]
ans = 0
for _ in range(n):
  a,b,c,d = map(int,input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

ab_dic = {}

# A와 B로 만들 수 있는 모든 경우의 수
for i in A:
  for j in B:
    ab_dic[i+j] = ab_dic.get(i+j,0) + 1

# C와 D로 만들 수 있는 모든 경우의 수
for i in C:
  for j in D:
    ans += ab_dic.get(-(i+j),0) # -부호로 들어가야함. 그래야 0이 돼서

print(ans)