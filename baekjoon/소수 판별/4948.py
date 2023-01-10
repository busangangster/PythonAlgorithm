# 소수를 반복문 돌릴때마다 찾으려면 시간이 많이 들기 때문에 시간초과가 날 수밖에 없음
# 그렇기에 범위 안에 있는 모든 소수들을 찾아서, 리스트에 저장해두고
# 실제 값을 구할 때, 범위 안에 있는 소수들만 리스트에서 뽑아서 쓰는 방식

_list = []
for i in range(1,246912):
  if i == 1:
    continue
  for j in range(2,int(i**0.5)+1):
    if i%j == 0:
      break
  else:
    _list.append(i)

while True:
  n = int(input())
  cnt = 0
  if n == 0:
    break
  for i in _list:
    if n < i <= 2*n:
      cnt += 1

  print(cnt)

