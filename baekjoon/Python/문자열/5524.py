n = int(input())
for _ in range(n):
  s = input()
  ans =''
  for x in s:
    if x.isupper():
      ans += x.lower()
    else:
      ans += x
  print(ans)
  