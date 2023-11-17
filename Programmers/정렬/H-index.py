def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        # 인용된 횟수가 배열의 인용값보다 크거나 같으면 answer 리턴 
        if answer >= citations[i]:
            return answer
        answer += 1
    # 모든 논문이 기준에 맞게 인용되었을 경우 answer 리턴 
    return answer 