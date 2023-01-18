n = input().upper()
t = list(set(n))

a = []
for i in t:
  cnt = n.count(i)
  a.append(cnt)


if a.count(max(a)) > 1:
  print('?')
else:
  print(t[(a.index(max(a)))])
