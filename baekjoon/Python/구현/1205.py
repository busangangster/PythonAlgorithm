import sys
input = sys.stdin.readline
n,score,p = map(int,input().split())

if n == 0: # 랭킹 리스트에 점수가 없을 경우
  print(1) # 무조건 1등
  sys.exit()
else:
  a = list(map(int,input().split()))
  # 점수의 개수와 랭킹 리스트 안의 점수 수가 같고 랭킹 리스트의 젤 낮은 점수가 score보다 클 경우
  if len(a) == p and a[-1] >= score: 
    print(-1) # 랭킹 리스트에 넣을 수 없음 
    sys.exit()

  elif len(a) == p: # 랭킹 리스트 길이와 p가 같을 경우
    for i in range(len(a)):
      if score >= a[i]: # score보다 낮은 점수를 발견하면
        a.insert(i,score) # 그 위치에 넣고
        a.pop() # 젤 낮은 점수는 제거. == 한 칸씩 밀리는 개념 
        break

  else: # 랭킹 리스트 안에 여유가 있는 경우 
    for i in range(len(a)):
      if score >= a[i]: # 낮은 점수 발견시 그 위치에 넣어줌 
        a.insert(i,score)
        break

rank = 1  # 순위는 1등부터
for x in a:
  if x > score: # 큰 점수는 rank 1씩 증가
    rank += 1
  elif x == score: # 같을 경우, 점수의 등수 중 가장 낮은 등수를 출력
    print(rank)
    break
else: # for문이 break 없이 정상종료 된 경우 rank 출력
  print(rank)