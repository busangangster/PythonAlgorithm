n = input().upper()
t = list(set(n)) # 중복을 제거하기 위해 set 자료구조 사용

a = []
for i in t:
  cnt = n.count(i)
  a.append(cnt)


if a.count(max(a)) > 1:
  print('?')
else:
  print(t[(a.index(max(a)))])

