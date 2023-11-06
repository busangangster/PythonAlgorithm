import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
line = []
for i in range(n,0,-1): # 키가 큰 사람부터
  line.insert(a[i-1],i) # 자기 앞에 몇명이 있는지를 인덱스로 지정한 뒤 insert

print(*line)
