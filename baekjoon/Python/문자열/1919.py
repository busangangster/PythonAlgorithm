a = input()
b = input()
ans = [0] * 26
result = 0

for x in a:
  ans[ord(x)-97] += 1

for x in b:
  ans[ord(x)-97] -= 1

for i in ans:
  result += abs(i)
print(result)