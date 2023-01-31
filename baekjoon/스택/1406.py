# 두개의 stack을 만들어서 cursor의 위치를 조절한다. 
# 스택 a에서 b로 옮겨가면 cursor은 왼쪽으로 이동한것이고
# 스택 b에서 a로 옮겨가면 cursor은 오른쪽으로 이동한 것임
import sys

st1 = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
st2 =[]

for _ in range(m):
  a = list(sys.stdin.readline().split())
  if a[0] == 'L':
    if st1:
      st2.append(st1.pop())
  elif a[0] == 'B':
    if st1:
      st1.pop()
  elif a[0] == 'D':
    if st2:
      st1.append(st2.pop())
  else:
    st1.append(a[1])

# st2를 reversed 해주는 이유는 st2 리스트에는 들어간 순서대로 append 되어 있기 때문에
st1.extend(reversed(st2))

for x in st1:
  print(x,end='')