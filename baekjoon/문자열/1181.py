import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
  word = sys.stdin.readline().strip() # 연속으로 값을 입력받는 for문에서는 공백제거 해줘야 함
  a.append(word)

b = set(a) # 중복제거를 위해 set으로 자료구조 변경
a = list(b) # sort 함수를 사용하기 위해 리스트로 다시 바꿔줌 
a.sort() # 사전순으로 오름차순 정렬
a.sort(key = len) # 길이순으로 오름차순 정렬

for x in a:
  print(x)

