import sys
input = sys.stdin.readline

ans = []
for i in range(1,6):
  s = input().strip()
  for j in range(len(s)-2):
    if s[j:j+3] == "FBI":
      ans.append(i)
      break

if not ans:
  print("HE GOT AWAY!")
else:
  print(*ans)

