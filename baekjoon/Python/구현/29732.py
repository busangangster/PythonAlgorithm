import sys
import copy
input = sys.stdin.readline

n,m,k = map(int,input().split())
a = [0] + list(input().strip()) # 인덱스번호 1부터 사용하려고 0 추가
aa = copy.deepcopy(a) # 바이러스가 퍼지는 것을 저장하는 리스트

for i in range(1,n+1):
  if a[i] == 'R':
    t,g = max(1,i-k),min(n,i+k) # 1일 후에 바이러스가 퍼지는 범위
    for j in range(t,g+1): # 범위 만큼 aa리스트에 바이러스 걸린 사람을 체크해줌
      aa[j] = 'R'

if aa.count('R') <= m: # 바이러스에 감염된 사람보다 치료제가 많거나 같은 경우
  print('Yes')
else:
  print('No')   
