n = input()
word = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in word:
  n = n.replace(i,'a') # word 안에 들어있는 문자를 'a'로 변경

# 반복문을 다 돌면 n = 'aeaaak'가 나옴
print(len(n))
