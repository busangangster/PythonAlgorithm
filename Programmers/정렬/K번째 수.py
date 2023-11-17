
def solution(array, commands):
    answer = []
    # 0을 array에 추가해줌으로써 인덱스를 1부터 시작할 수 있도록
    array.insert(0,0)
    for x in commands:
        cur = array[x[0]: x[1]+1] # cur이라는 변수에 i ~ k번째 까지의 수를 저장
        cur.sort() # 정렬
        answer.append(cur[x[2]-1]) # j번째 수 answer에 추가 
        
    return answer