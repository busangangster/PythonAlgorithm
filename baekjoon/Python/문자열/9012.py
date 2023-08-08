# 핵심 포인트: 갯수가 맞는 게 중요한 것이 아니라
# ')'가 나올 때 그 앞에 '('가 하나라도 있어야 함
t = int(input())

for _ in range(t):
  a = input()
  _list = []
  for i in a:
    if i == '(':
      _list.append(i)
    else:
      if _list:
        _list.pop()
      else:
        print('NO')
        break
  else:
    if _list:
      print('NO')
    else:
      print('YES')




  
    