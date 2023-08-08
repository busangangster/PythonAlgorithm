import sys
input = sys.stdin.readline

a = input().strip()
stack = []
ucpc = ['U','C','P','C']

for x in a:
  if ucpc:
    if x == ucpc[0]:
      stack.append(x)
      ucpc.pop(0)

if stack and stack == ['U','C','P','C']:
  print('I love UCPC')
else:
  print('I hate UCPC')


