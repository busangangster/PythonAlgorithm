import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  arr = []
  cnt = 0
  check = [False] * 1001 # 나눠주는 책 체크
  for _ in range(m):
    arr.append(list(map(int,input().split())))

    arr.sort(key = lambda x:x[1]) # 각 리스트의 두번째 수를 기준으로 오름차순 정렬

  for i,k in arr:
    for j in range(i,k+1): # 주어진 구간 안에서
      if check[j] == False: # 아직 책이 있다면
        check[j] = True # 책을 주고, cnt를 + 1
        cnt += 1
        break

  print(cnt)


