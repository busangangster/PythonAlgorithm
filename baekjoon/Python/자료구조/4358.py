import sys
input = sys.stdin.readline

dic = {}
num = 0
while True: # 값이 들어오지 않을때까지 반복
    a = input().strip()
    if a == '': 
       break
    num += 1 # 나무의 총 갯수 확인
    if a in dic: # 이미 나무가 딕셔너리에 존재하면 1 증가
      dic[a] += 1
    else: # 존재하지 않으면 새롭게 생성 
      dic[a] = 1

dd = sorted(dic) # key기준 오름차순으로 정렬

for i in dd:
   k = dic[i]
   print(i,end=' ') # 나무 이름 출력하고 이어서,
   # f-string으로 소수점 4번째자리까지 반올림해서 출력
   print("%.4f" %(k / num * 100)) # 백분율 구해주기
