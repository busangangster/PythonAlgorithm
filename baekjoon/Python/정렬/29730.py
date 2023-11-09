import sys
input = sys.stdin.readline

n = int(input())
baekjoon = []
others = []
for _ in range(n):
  a = input().strip()
  if a[:6] == 'boj.kr': # 백준으로 시작하는 경우
    baekjoon.append(a) # 따로 저장
  else:
    others.append(a)

others.sort(key = lambda x:(len(x),x)) # 일반 공부들은 문자열 길이, 사전순 정렬

r = []
for x in baekjoon: # 백준 공부는 문제번호로 정렬하기 위해 '/'을 기준으로 나눔
  s = x.split('/')
  r.append(s)

r.sort(key = lambda x:int(x[1])) # 나눈 것을 오름차순 정렬

for x in others: # 다른 공부 먼저 출력하고
  print(x)

for x in r: # 백준 공부 출력
  t = '/'.join(map(str,x))
  print(t)