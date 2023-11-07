import sys
input = sys.stdin.readline

a = input().strip()
ans = 0
stack = []
for i in range(len(a)):
  if not stack:
    stack.append(a[i])
    ans += 10
  else:
    if stack[-1] == a[i]:
      ans += 5
    else:
      stack.append(a[i])
      ans += 10
  
print(ans)