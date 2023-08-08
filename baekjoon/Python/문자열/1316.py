n = int(input())
word =''
cnt = 0

for i in range(n):
  a = input()
  _list = []
  for j in a:
    if j != word and j in _list:
      break
    else:
      word = j
      _list.append(j)
  else:
    cnt += 1

print(cnt)
    