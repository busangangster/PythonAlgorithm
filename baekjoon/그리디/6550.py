import sys
input = sys.stdin.readline

while True:
  try:
    s,t = map(str,input().split())
    first = list(s) # 입력받은 s를 리스트 형태로 변환
    for i in t: # 문자열 t안의 알파벳이 
      # 리스트가 비어있지 않고, first의 첫번째 알파벳과 같다면
      if first and i == first[0]:  
        first.pop(0) # 리스트에서 해당 알파벳 제거. 
    
    if not first: # 리스트가 비어있으면, 부분문자열 가능 
      print('Yes')
    else: # 비어있지 않으면 안됨 
      print('No')

  except:
    break