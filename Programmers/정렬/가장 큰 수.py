

def solution(numbers):
    n_numbers = list(map(str,numbers))
    n_numbers.sort(key = lambda x: x*3, reverse = True)
    # n_numbers의 원소들을 answer에 join 해줌 
    answer = ''.join(n_numbers)
    # answer를 수로 변환하고 다시 문자열로 변환
    # why ? 반례 [0,0,0,0] 
    answer = str(int(answer))
    return answer
