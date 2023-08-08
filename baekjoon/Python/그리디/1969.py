import sys
input = sys.stdin.readline
n,m = map(int,input().split())

dna = []
ans = ''
cnt = 0
for _ in range(n):
  dna.append(input().strip())

for i in range(m):
  g = [] # 세로로 한줄을 읽을 때마다 리스트 초기화
  dict = {} # 딕셔너리 초기화 
  for j in range(len(dna)): # 세로로 한줄씩 리스트에 append하기
    g.append(dna[j][i])

  g.sort() # 횟수가 중복되는 경우 사전순으로 출력하기 위한 정렬
  for x in g: # 각 알파벳이 몇번 등장하는 지 횟수 dict에 저장
    if dict.get(x) == None:
      dict[x] = 1
    else:
      dict[x] += 1
  
  # value가 최대값인 key를 max_al 변수에 저장 
  max_al = max(dict,key = dict.get)
  ans +=  max_al

for x in dna: # Hamming Distance 구하기 
  for i in range(m):
    if ans[i] != x[i]:
      cnt += 1

print(ans)
print(cnt)


