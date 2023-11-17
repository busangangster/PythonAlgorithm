from collections import deque
def solution(progresses, speeds):
    answer = []
    times = 0
    cnt = 0
    n_progresses = deque(progresses)
    n_speeds = deque(speeds)
    while n_progresses:
        if n_progresses[0] + times*n_speeds[0] >= 100:
            n_progresses.popleft()
            n_speeds.popleft()
            cnt += 1
        else:
            times += 1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
    answer.append(cnt)
            
    return answer