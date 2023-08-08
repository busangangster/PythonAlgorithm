n = input()
alpha = list(range(97,123)) # a~z까지 아스키코드로 배열 만들기

# find 함수는 찾는 문자가 문자열에 포함되어 있지 않으면 '-1'을 출력
for x in alpha:
  # 찾은 아스키코드를 문자로 변환해서 인덱스 찾기
  print(n.find(chr(x)),end=' ') 
