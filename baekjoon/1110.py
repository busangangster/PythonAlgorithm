n = int(input())
cnt = 0

start = n # 새로운 수를 만들기 위해 시작하는 값

while True:
  first = (start // 10) + (start % 10) # 십의 자리와 일의 자리를 더함
  # 더한 값이 1의 자리로, 기존 값의 일이 자리가 십의 자리로 가야함
  result = (first % 10) + (start % 10 * 10) 
  start = result # 한번의 연산이 끝나면 수 만들기 시작값은 바뀜
  cnt += 1
  if result == n: # 만드는 값이 입력 값과 같아지면 종료
    print(cnt)
    break


