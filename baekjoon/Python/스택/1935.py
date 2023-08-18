import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
arr = []
stack = []

for _ in range(n):
  arr.append(int(input()))

for i in a:
  if i.isalpha():
    # 수가 저장되어 있는 배열 arr에 인덱스로 접근할 때 해당 알파벳의 아스키 코드를 사용함 
    stack.append(arr[ord(i) - 65])
  else:
    if i == '+':
      t = stack[-2] + stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    elif i == '-':
      t = stack[-2] - stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    elif i == '*':
      t = stack[-2] * stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    else:
      t = stack[-2] / stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)

print("{:.2f}".format(stack[0]))
